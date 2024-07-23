# Little Lemon - Backend application
Little Lemon is a personal backend application developed using Django Rest framework which serves api's for imaginary restaurant "Little Lemon"

## Tech Stack
* Python
* Django
* Django Rest Framework

## Project Requirement
Building the backend application for a imaginary restaurant* "`Little Lemon`"

### The Backend application should consist of the following operations
* User Creation / Modification
* Order Creation / Modification
* Menu Creation / Modification
* Adding / Deleting Items in Cart
* Assigning deliveries / Updating statuses of Orders
* Assigning users to groups

## Project Structure
* Project folder: LittleLemonProject
    * urls.py
    * settings.py
> `Note: above mentioned are the part of those files which had changes included as part of the project`
* Project App: LittleLemonApp
    * urls.py
    * settings.py
    * views.py
    * models.py
    * serializers.py
> `Note: above mentioned are the part of those files which had changes included as part of the app`

## Functional Design
* Users are categorized under three roles and are assigned groups respectively
    > * The operations are made available based on the user group 
* Customer:
    * Operations allowed for a customer
        > * User creation, token generation and view user details
        > * Access Menu items
        > * Add or delete items to Cart
        > * Create Orders or View Order History
* Manager:
    > * User creation, token generation and view user details
    > * Assign / Remove users from groups 
    > * Create, View, Delete Menu items
    > * View, Update, Delete Orders
        > * Assign Orders to delivery crew
* Delivery Crew:
    > * View / Update user details
    > * View assigned orders for deliveries or Update status of the delivered orders
* Admin:
    > * Admin is the superuser and has access to all the operations without any restrictions
    > `Note: User groups are created and maintained by admin`
        > * Managers & DeliveryCrew are the two user groups available

# Technical Design
### Libraries
> Python V3.12.3
> >  Djoser V 2.2.3

> >  Django V5.0.7
> >   * Djangorestframework V3.15.2

## Code Flow:
### Processing Logic:
* Following outlines the usecases of api endpoints along with screenshots
## User Registration
<table>
  <tr>
    <td><h2>End point</h2></td>
    <td><h2>Role</h2></td>
    <td><h2>Method</h2></td>
    <td><h2>Purpose</h2></td>
    <td><h2>Request</h2></td>
    <td><h2>Response</h2></td>
  </tr>
  <tr>
    <td>/api/users</td>
    <td>No role required</td>
    <td>POST</td>
    <td>Creates a new user with username, email,first_name,last_name and password</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/01_user_creation_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/01_user_creation_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/users/users/me/</td>
    <td>Anyone with a valid user token</td>
    <td>GET</td>
    <td>Displays only the current user</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/02_user_details_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/02_user_details_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/token/login/</td>
    <td>Anyone with a valid username and password</td>
    <td>POST</td>
    <td>Generates access tokens that can be used in other API calls in this project</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/03_token_creation_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/03_token_creation_ins_res.JPG"/></td>
  </tr>
</table>

## Menu-items endpoints
<table>
  <tr>
    <td><h2>End point</h2></td>
    <td><h2>Role</h2></td>
    <td><h2>Method</h2></td>
    <td><h2>Purpose</h2></td>
    <td><h2>Request</h2></td>
    <td><h2>Response</h2></td>
  </tr>
  <tr>
    <td>/api/menu-items</td>
    <td>Customer, delivery crew</td>
    <td>GET</td>
    <td>Lists all menu items. Return a 200 – Ok HTTP status code</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/04_get_menu_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/04_get_menu_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items</td>
    <td>Customer, delivery crew</td>
    <td>POST, PUT, PATCH, DELETE</td>
    <td>Denies access and returns 401 – Unauthorized HTTP status code</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/04_put_menu_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/04_put_menu_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items/{menuItem}</td>
    <td>Customer, delivery crew</td>
    <td>GET</td>
    <td>Lists single menu item</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/06_get_menu_id_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/06_get_menu_id_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items/{menuItem}</td>
    <td>Customer, delivery crew</td>
    <td>POST, PUT, PATCH, DELETE</td>
    <td>Returns 401 - Unauthorized</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/06_pu_menu_id_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/06_pu_menu_id_ins_res.JPG"/></td>
  </tr>
   <tr>
    <td>/api/menu-items</td>
    <td>Manager</td>
    <td>GET</td>
    <td>Lists all menu items. Return a 200 – Ok HTTP status code</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/07_get_menu_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/07_get_menu_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items</td>
    <td>Manager</td>
    <td>POST</td>
    <td>Creates a new menu item and returns 201 - Created</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/08_post_menu_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/08_post_menu_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items/{menuItem}</td>
    <td>Manager</td>
    <td>GET</td>
    <td>Lists single menu item</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/09_get_menu_id_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/09_get_menu_id_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items/{menuItem}</td>
    <td>Manager</td>
    <td>PUT, PATCH</td>
    <td>Updates single menu item</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/10_put_menu_id_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/10_put_menu_id_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/menu-items/{menuItem}</td>
    <td>Manager</td>
    <td>DELETE</td>
    <td>Deletes menu item</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/11_del_menu_id_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/11_del_menu_id_mgr_ins_res.JPG"/></td>
  </tr>
</table>

## User group management endpoints
<table>
  <tr>
    <td><h2>End point</h2></td>
    <td><h2>Role</h2></td>
    <td><h2>Method</h2></td>
    <td><h2>Purpose</h2></td>
    <td><h2>Request</h2></td>
    <td><h2>Response</h2></td>
  </tr>
  <tr>
    <td>/api/groups/manager/users</td>
    <td>Manager</td>
    <td>GET</td>
    <td>Returns all managers</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/12_get_managers_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/12_get_managers_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/groups/manager/users</td>
    <td>Manager</td>
    <td>POST</td>
    <td>Assigns the user in the payload to the manager group and returns 201-Created</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/13_post_create_manager_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/13_post_create_manager_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/groups/manager/users/{userId}</td>
    <td>Manager</td>
    <td>DELETE</td>
    <td>Removes this particular user from the manager group and returns 200 – Success if everything is okay.</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/14_del_manager_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/14_del_manager_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/groups/delivery-crew/users</td>
    <td>Manager</td>
    <td>GET</td>
    <td>Returns all delivery crew</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/15_get_dc_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/15_get_dc_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/groups/delivery-crew/users</td>
    <td>Manager</td>
    <td>POST</td>
    <td>Assigns the user in the payload to delivery crew group and returns 201-Created HTTP</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/16_create_dc_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/16_create_dc_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/groups/delivery-crew/users/{userId}</td>
    <td>Manager</td>
    <td>DELETE</td>
    <td>Removes this user from the manager group and returns 200 – Success if everything is okay.If the user is not found, returns  404 – Not found</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/17_del_dc_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/17_del_dc_mgr_ins_res.JPG"/></td>
  </tr>
</table>

## Cart management endpoints
<table>
  <tr>
    <td><h2>End point</h2></td>
    <td><h2>Role</h2></td>
    <td><h2>Method</h2></td>
    <td><h2>Purpose</h2></td>
    <td><h2>Request</h2></td>
    <td><h2>Response</h2></td>
  </tr>
  <tr>
    <td>/api/cart/menu-items</td>
    <td>Customer</td>
    <td>GET</td>
    <td>Returns current items in the cart for the current user token</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/18_get_cart_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/18_get_cart_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/cart/menu-items</td>
    <td>Customer</td>
    <td>POST</td>
    <td>Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/19_add_items_to_cart_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/19_add_items_to_cart_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/cart/menu-items</td>
    <td>Customer</td>
    <td>DELETE</td>
    <td>Deletes all menu items created by the current user token</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/20_del_cart_items_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/20_del_cart_items_ins_res.JPG"/></td>
  </tr>
</table>

## Order management endpoints
<table>
  <tr>
    <td><h2>End point</h2></td>
    <td><h2>Role</h2></td>
    <td><h2>Method</h2></td>
    <td><h2>Purpose</h2></td>
    <td><h2>Request</h2></td>
    <td><h2>Response</h2></td>
  </tr>
  <tr>
    <td>/api/orders</td>
    <td>Customer</td>
    <td>GET</td>
    <td>Returns all orders with order items created by this user</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/21_get_orders_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/21_get_orders_ins_req.JPG"/></td>
  </tr>
  <tr>
    <td>/api/orders</td>
    <td>Customer</td>
    <td>POST</td>
    <td>Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/22_post_orders_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/22_post_orders_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/orders/{orderId}</td>
    <td>Customer</td>
    <td>GET</td>
    <td>Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/23_get_orders_id_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/23_get_orders_id_ins_res.JPG"/></td>
  </tr>

  <tr>
    <td>/api/orders</td>
    <td>Manager</td>
    <td>GET</td>
    <td>Returns all orders with order items by all users</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/24_get_orders_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/24_get_orders_mgr_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/orders/{orderId}</td>
    <td>Manager</td>
    <td>PUT, PATCH</td>
    <td>Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1.If a delivery crew is assigned to this order and the status = 0, it means the order is out for delivery.If a delivery crew is assigned to this order and the status = 1, it means the order has been delivered.</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/25_put_mgr_assign_dc_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/25_put_mgr_assign_dc_ins_res.JPG"/></td>
  </tr>
  <tr>
    <td>/api/orders/{orderId}</td>
    <td>Manager</td>
    <td>DELETE</td>
    <td>Deletes this order</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/28_del_order_orderid_mgr_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/28_del_order_orderid_mgr_ins_res.JPG"/></td>
  </tr>

  <tr>
    <td>/api/orders</td>
    <td>Delivery Crew</td>
    <td>GET</td>
    <td>Returns all orders with order items assigned to the delivery crew</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/26_get_dc_orders_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/26_get_dc_orders_ins_res_with_orders.JPG"/></td>
  </tr>
  <tr>
    <td>/api/orders/{orderId}</td>
    <td>Delivery Crew</td>
    <td>PATCH</td>
    <td>A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.</td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/27_patch_dc_order_updt_ins_req.JPG"/></td>
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/27_patch_dc_order_updt_ins_res.JPG"/></td>
  </tr>
</table>

`Note: Pagination is used for returning all the orders in the system when Manager invokes the GET request to orders api endpoint`

## Tools 
* Insomnia is used for calling api endpoints
> `Note: Browsable api provided by Django is also used to validate the functionality`