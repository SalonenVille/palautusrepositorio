*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  jake  jake12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  jake  jake12345
    Create User  jake  jake12345
    Output Should Contain  User with username jake already exists

Register With Too Short Username And Valid Password
    Create User  ja  jake12345
    Output Should Contain  Username must contain atleast 3 letters

Register With Enough Long But Invalid Username And Valid Password
    Create User  222  jake12345
    Output Should Contain  Username must only contain letters

Register With Valid Username And Too Short Password
    Create User  jake  jake123
    Output Should Contain  Password must contain atleast 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  jake  jakensalis
    Output Should Contain  Password must contain numbers
    