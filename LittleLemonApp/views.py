from rest_framework import generics,permissions
from rest_framework.exceptions import NotFound
from .models import MenuItem, Category, Cart,Order,OrderItem
from .serializers import MenuItemSerializer,CategorySerializer,CustomUserRegistrationSerializer, CartItemsSerializer, OrderSerializer, OrderItemSerializer,OrderUpdateSerializer,OrderStatusSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.contrib.auth.models import Group,User
from rest_framework.exceptions import PermissionDenied

import datetime
class UserDetails(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=CustomUserRegistrationSerializer
    def get(self,request):
        return Response({"message":"GET method is available at users/users/me/"},status=status.HTTP_200_OK)
class UserSepcificDetails(generics.ListAPIView):
    serializer_class=CustomUserRegistrationSerializer
    def get_queryset(self):
        userinfo=getUserInfo(self.request.user)
        if(userinfo=='AD' or userinfo=='MN'):
            test_data = User.objects.all()
            print(test_data)
            return User.objects.all()
        elif(userinfo=='AN' or userinfo=='DC'):
            return User.objects.filter(username=self.request.user)
    def get(self,request):
        return self.list(request,status=status.HTTP_200_OK)
# function to fetch userinfo
def getUserInfo(request):
    # print('came inside the getUserInfo')
    # print(request)
    user = request
    # print(user,' is the user')
    userType = ''
    if(user.groups.filter(name='DeliveryCrew').exists()):
        userType = 'DC'
    elif(user.groups.filter(name='Managers').exists()):
        userType = 'MN'
    elif(user.groups.filter(name='Admin').exists()):
        userType = 'AD'
    else:
        userType = 'AN'
    return userType
    # note: User group definitions AN - Anonymous, DC - Delivery Crew, MN - Managers, AD - Admin
# HTTP_204_NO_CONTENT in insomnia there is no response body getting displayed hence putting HTTP_200_OK instead of 204 status
# Function based Category view to view and add
@api_view(['GET','POST'])
def CategoryView(request):
    user = getUserInfo(request.user)
    if(request.method=='GET'):
        category = Category.objects.all()
        serialized_item=CategorySerializer(category,many=True)
        if not serialized_item.data:
            return Response({"message":"Category not available"},status=status.HTTP_200_OK) # HTTP_204_NO_CONTENT
        return Response(serialized_item.data)
    elif(request.method=='POST'):
        if(user == 'AN' or user =='DC'):
            return Response({"message":"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
        print(request.data)
        serialized_item = CategorySerializer(data=request.data)
        if(serialized_item.is_valid(raise_exception=True)):
            serialized_item.save()
            return Response(serialized_item.data,status=status.HTTP_201_CREATED)
        return Response (serialized_item.errors,status=status.HTTP_400_BAD_REQUEST)

# Function based Category view to update, delete and partial-update record based on the id
@api_view(['DELETE','GET','PUT','PATCH'])
def CategoryUpdate(request,pk):
    user = getUserInfo(request.user)
    print('User: ',request.user,', User-Group: ',user)
    try:
        category = get_object_or_404(Category,pk=pk)
    except Exception:
        return Response({"message":"No Categories found"},status=status.HTTP_200_OK)
    if(request.method=='GET'):
        serialized_item = CategorySerializer(category)
        return Response(serialized_item.data,status=status.HTTP_200_OK)
    if(user == 'AD' or user =='MN'):
        if(request.method=='DELETE'):
            category.delete()
            return Response({"message":"Category deleted"},status=status.HTTP_202_ACCEPTED)
        elif(request.method == 'PUT'):
            serialized_item = CategorySerializer(category, data=request.data)
            if serialized_item.is_valid(raise_exception=True):
                serialized_item.save()
                return Response({"message":"Category updated"},status=status.HTTP_202_ACCEPTED)
        elif(request.method=='PATCH'):
            serialized_item = CategorySerializer(category, data=request.data)
            if(serialized_item.is_valid(raise_exception=True)):
                serialized_item.save()
                return Response({"message":"Category partially updated"})
    else:
        return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    
# class based view function for fetching and creating menu items
class MenuItemView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        response_data = self.list(request,*args,**kwargs)
        if not response_data.data:
            return Response({"message":"Menu not available"},status=status.HTTP_200_OK) # HTTP_204_NO_CONTENT
        return self.list(request,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
            user = getUserInfo(request.user)
            if(user == 'AD' or user =='MN'):
                print(request.data)
                self.create(request,*args,**kwargs)
                return Response({"message":"Created new entry"},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    def put(sel,request):
        return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    def patch(sel,request):
        return Response({"message":"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
    def destroy(sel,request):
        return Response({"message":"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)

#class based view function for updating, partially updating and deleting menu items based on user group
class MenuItemUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    def get_object(self):
        try:
            return MenuItem.objects.get(pk=self.kwargs['pk'])
        except MenuItem.DoesNotExist:
            raise NotFound({"message":"Menu item not found"},code=status.HTTP_404_NOT_FOUND)
    def update(self,request,*args,**kwargs):
        user = getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            super().update(request,*args,**kwargs)
            return Response({"message":"Menu item updated"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    def destroy(self,request,*args,**kwargs):
            user = getUserInfo(request.user)
            if(user == 'AD' or user =='MN'):
                super().destroy(request,*args,**kwargs)
                return Response({"message":"Menu item deleted"},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)

# class based function for creating and fetching manager group users
class ManagerCreation(generics.ListCreateAPIView):
    queryset=User.objects.filter(groups__name='Managers')
    serializer_class=CustomUserRegistrationSerializer
    def get(self,request):
        user=getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            response_data = self.list(request)
            if not response_data:
                return Response({"message":"No Users under Managers group"},status=status.HTTP_200_OK) # HTTP_204_NO_CONTENT
            return self.list(request,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    def post(self,request):
        user = getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            user_instance = self.create(request).data
            user_id = user_instance['username']
            created_user = User.objects.get(username=user_id)
            managers_group = Group.objects.get(name='Managers')
            created_user.groups.add(managers_group)
            return Response({"message":"Created new user under Manager group"},status=status.HTTP_201_CREATED)
        return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
# class based view for deleting the manager user
class ManagerDeletion(generics.RetrieveDestroyAPIView):
    queryset=User.objects.filter(groups__name='Managers')
    serializer_class=CustomUserRegistrationSerializer
    def get_object(self):
        user=getUserInfo(self.request.user)
        if(user not in ['AD','MN']):
            raise PermissionDenied({"message":"Not Authorized"},code=status.HTTP_401_UNAUTHORIZED)
        try:
            return User.objects.get(pk=self.kwargs['pk'])
        except User.DoesNotExist:
            raise NotFound({"message":"User not found"},code=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, *args, **kwargs):
        user = getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            super().destroy(request,*args,**kwargs)
            return Response({"message":"User deleted"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)

# class based function for creating and fetching delivery crew group users
class DCrewCreation(generics.ListCreateAPIView):
    queryset=User.objects.filter(groups__name='DeliveryCrew')
    serializer_class=CustomUserRegistrationSerializer
    def get(self,request):
        user = getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            response_data = self.list(request)
            if not response_data:
                return Response({"message":"No Users under Delivery Crew group"},status=status.HTTP_200_OK) # HTTP_204_NO_CONTENT
            return self.list(request,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    def post(self,request):
        user = getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            user_instance = self.create(request).data
            user_id = user_instance['username']
            created_user = User.objects.get(username=user_id)
            managers_group = Group.objects.get(name='DeliveryCrew')
            created_user.groups.add(managers_group)
            return Response({"message":"Created new user under Delivery Crew group"},status=status.HTTP_201_CREATED)
        return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
# class based view for deleting the manager user
class DCrewDeletion(generics.RetrieveDestroyAPIView):
    queryset=User.objects.filter(groups__name='DeliveryCrew')
    serializer_class=CustomUserRegistrationSerializer
    def get_object(self):
        user=getUserInfo(self.request.user)
        if(user not in ['AD','MN']):
            raise PermissionDenied({"message":"Not Authorized"},code=status.HTTP_401_UNAUTHORIZED)
        try:
            return User.objects.get(pk=self.kwargs['pk'])
        except User.DoesNotExist:
            raise NotFound({"message":"User not found"},code=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, *args, **kwargs):
        user = getUserInfo(request.user)
        if(user == 'AD' or user =='MN'):
            super().destroy(request,*args,**kwargs)
            return Response({"message":"User deleted"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)

# function based view for adding items into the cart and fetching the cart details and deleting all the items from the cart
@api_view(['GET','POST','DELETE'])
@permission_classes([permissions.IsAuthenticated])
def CartAddFetchDelete(request):
    if request.method=='GET':
        cartitems= Cart.objects.filter(user=request.user)
        serialized_item=CartItemsSerializer(cartitems,many=True)
        if not serialized_item.data:
            return Response({"message":"Cart is Empty"},status=status.HTTP_200_OK) # HTTP_204_NO_CONTENT
        return Response(serialized_item.data)
    elif request.method=='POST':
        try:
            # print("came into POST method")
            serialized_item = CartItemsSerializer(data=request.data,context={'request': request})
            if(serialized_item.is_valid(raise_exception=True)):
                serialized_item.save()
                return Response(serialized_item.data,status=status.HTTP_201_CREATED)
            return Response (serialized_item.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            if 'UNIQUE constraint' in str(e):
                return Response({"message":"Item can be added only once"},status=status.HTTP_200_OK)
            elif 'Incorrect type' in str(e):
                return Response({"message":"Invalid Menu item"},status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        try:
            cartitems = Cart.objects.filter(user=request.user)
            if not cartitems:
                return Response({"message":"Cart Empty"},status=status.HTTP_200_OK)    
            cartitems.delete()
            return Response({"message":"Cart Deleted"},status=status.HTTP_200_OK)
        except Exception:
            return Response({"message":"Internal issue while deleting the records, please try again"},status=status.HTTP_200_OK)        
    elif request.method=='PUT' or request.method=='PATCH':
        return Response({"message":"Sha Operation Not Allowed"},status=status.HTTP_200_OK)

# class based view for orders fetching and creating
def fetchDestroyCartItems(user,val):
        cartinfo = Cart.objects.filter(user=user)
        if val=='FETCH':
            # print('inside the cartitems ',cartinfo)
            return cartinfo
        elif val=='DESTROY':
            try:
                cartinfo.delete()
                return('SUCCESS')
            except Exception as e:
                print(e+' >> '+str(e))
                return('ERROR')
def createOrderItems(vals,order_instance):
    menuitem_instance= MenuItem.objects.get(pk=vals['menuitem'])
    try:
        create_orderitem=OrderItem.objects.create(
            order=order_instance,
            menuitem=menuitem_instance,
            quantity=vals['quantity'],
            price=vals['price'],
            unit_price=vals['unit_price']    
        )
        print('printing orderitem :',create_orderitem)
        return 'SUCCESS'
    except Exception as e:
        print(str(e))
        return 'ERROR'
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
class OrderFetchCreate(generics.ListCreateAPIView):
    serializer_class=OrderSerializer
    def get_queryset(self):
        # print('User infor in OrderFetch: ',self.request.user)
        user = getUserInfo(self.request.user)
        # print(user,' is the user after fetching in orderfecth')
        print('User name: '+str(self.request.user)+' user stat: '+user)
        if(user == 'AD' or user =='MN'):
            return Order.objects.all()
        elif(user=='AN'):
            return Order.objects.filter(user=self.request.user)
        elif(user=='DC'):
            return Order.objects.filter(delivery_crew=self.request.user)
    def get(self,request):
        # # following block is without pagination
        # response_data = self.list(request)
        # if not response_data.data:
        #     return Response({"message":"No orders to display"},status=status.HTTP_200_OK)
        # return self.list(request,status=status.HTTP_200_OK)

        #following block is with pagination
        queryset = self.get_queryset()
        perpage = request.query_params.get('perpage',default=2)
        reqpage = request.query_params.get('page',default=1)
        print(reqpage,' is perpage')
        print(reqpage,' is page')
        paginator = Paginator(queryset,per_page=perpage)
        try:
            orders=paginator.page(reqpage)
        except PageNotAnInteger:
            return Response({"message":"Invalid page number"},status=status.HTTP_200_OK)
        except EmptyPage:
            return Response({"message":"Page number exceeds the maximum pages"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"Error during pagination"},status=status.HTTP_200_OK)
        serialized_orders = OrderSerializer(orders,many=True)
        if not serialized_orders.data:
            return Response({"message":"No orders to display"},status=status.HTTP_200_OK)
        response_data={
            'orders':serialized_orders.data,
            'total_pages':paginator.num_pages,
            'current_page':int(reqpage),
            'total_items':paginator.count
        }
        return Response(response_data,status=status.HTTP_200_OK)
    def post(self,request):
        user = getUserInfo(request.user)
        print('User name: '+str(self.request.user)+' user stat: '+user)
        if(user=='AN'):
            cartdata=fetchDestroyCartItems(request.user,'FETCH')
            cart_serializer=CartItemsSerializer(cartdata,many=True)
            # print(cart_serializer.data,' this is cart data')
            if not cart_serializer.data:
                return Response({"message":"Cart is empty, please add items before ordering"},status=status.HTTP_200_OK)
            currtime=datetime.datetime.now()
            price=0
            # print(cart_serializer.data)
            for vals in cart_serializer.data:
                price= price + float(vals['price'])
            try:
                created_order=Order.objects.create(
                    user=request.user,
                    total=price,
                    date=currtime                
                )
                print(created_order.id)
                for vals in cart_serializer.data:
                    orderitems=createOrderItems(vals,created_order)
                    print('printing orderitems ',orderitems)
                    if orderitems=='SUCCESS':
                        delCart = fetchDestroyCartItems(request.user,'DESTROY')
                        print(delCart)
                        if delCart=='SUCCESS':
                            return Response({"message":"Order created and will be delivered soon","orderid":created_order.id},status=status.HTTP_201_CREATED)
                        else:
                            return Response({"message":"Error while deleting the cart, please delete it manaully"},status=status.HTTP_501_NOT_IMPLEMENTED)
                    elif orderitems=='ERROR':
                        try:
                            deletingOrder=Order.objects.filter(id=created_order.id)
                            deletingOrder.delete()
                            print(deletingOrder)
                            return Response({"message":"Error while creating the order, please retry again"},status=status.HTTP_501_NOT_IMPLEMENTED)
                        except Exception as e:
                            print('error in deletion of record in order table '+str(e))
                            return Response({"message":"Error while creating the order, please retry again"},status=status.HTTP_501_NOT_IMPLEMENTED)
                # return Response({"message":"Order created and will be delivered soon","orderid":created_order.id},status=status.HTTP_201_CREATED)
            except Exception:
                return Response({"message":"Error while creating the order, please retry again"},status=status.HTTP_501_NOT_IMPLEMENTED)
        return Response({"message":"Orders can be submitted under customer login only"},status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT','PATCH','DELETE','GET'])
def OrderUpdates(request,pk):
    userinfo = getUserInfo(request.user)
    try:
        orderdetails=Order.objects.get(pk=pk)
    except Exception as e:
        print(str(e))
        return Response ({"message":"unable to fetch the order details, please try again or check order number"},status=status.HTTP_200_OK)
    if(request.method=='PUT'):
        if(userinfo=='AD' or userinfo=='MN'):
            if not request.data.get('delivery_crew'):
                return Response({"message":"delivery crew id 'delivery_crew' is must"},status=status.HTTP_200_OK)
            order_assign_dc = OrderUpdateSerializer(orderdetails,data=request.data)
            if order_assign_dc.is_valid(raise_exception=True):
                try:
                    order_assign_dc.save()
                    return Response({"message":"Order details updated, assigned to delivery crew"},status=status.HTTP_202_ACCEPTED)
                except Exception as e:
                    print(str(e))
                    return Response({"message":"Order could not be assigned, please try again or check order number"},status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        if(userinfo=='DC'):
            if not request.data.get('status'):
                return Response({"message":"status is must"},status=status.HTTP_200_OK)
            order_status_update = OrderStatusSerializer(orderdetails,data=request.data)
            if order_status_update.is_valid(raise_exception=True):
                try:
                    order_status_update.save()
                    return Response({"message":"Order status updated as delivered by "+str(request.user)},status=status.HTTP_202_ACCEPTED)
                except Exception as e:
                    print(str(e))
                    return Response({"message":"Order status could not be updated, please try again or check order number"},status=status.HTTP_200_OK)
    elif(request.method=='DELETE'):
        if(userinfo=='AD' or userinfo=='MN'):
            try:
                orderdetails.delete()
                return Response({"message":"Order id "+str(pk)+" is deleted"},status=status.HTTP_202_ACCEPTED)
            except Exception as e:
                print(str(e))
                return Response({"message":"Order could not be deleted, please retry later or check order number "+request.user},status=status.HTTP_200_OK)
    elif(request.method=='GET'):
        if(userinfo=='AN'):
            try:
                fullorderinfo = OrderItem.objects.filter(order_id=pk)
                orderinfo_serializer=OrderItemSerializer(fullorderinfo,many=True)
                if not orderinfo_serializer.data:
                    return Response ({"message":"No items under the order id "+str(pk)},status=status.HTTP_200_OK)
                print('serialized data ',orderinfo_serializer.data)
                print('serializer ',orderinfo_serializer)
                return Response(orderinfo_serializer.data,status=status.HTTP_200_OK)
            except Exception as e:
                return Response ({"message":"unable to fetch the order details, please try again or check order number"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Order details will be displayed for customer logins only "+str(request.user)},status=status.HTTP_200_OK)