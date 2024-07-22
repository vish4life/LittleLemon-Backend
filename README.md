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
    > * Based on the user the operations are made available
* Customer:
    * Operations allowed for a customer
        > * User creation, token generation and view details
        > * Access Menu items
        > * Add or delete items to Cart
        > * Create Orders or View Order History
* Manager:
    > * User creation, token generation and view details
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
> > Django V5.0.7
> > * Djangorestframework V3.15.2
> > Djoser V 2.2.3

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
    <td><img src = "https://github.com/vish4life/LittleLemon-Backend/blob/main/Snapshots_Usecase/01_user_creation_ins_req.JPG" width='600' height='350' /></td>
    <td></td>
  </tr>
  <tr>
    <td>/api/users/users/me/</td>
    <td>Anyone with a valid user token</td>
    <td>GET</td>
    <td>Displays only the current user</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>/token/login/</td>
    <td>Anyone with a valid username and password</td>
    <td>POST</td>
    <td>Generates access tokens that can be used in other API calls in this project</td>
    <td></td>
    <td></td>
  </tr>
</table>