from pydantic import BaseModel, Field, EmailStr, field_validator


class UserCreate(BaseModel):
    """
    Represents the structure and validation logic for creating a new user in the system.

    This class is used to handle user input during the user registration process. It ensures that
    the user's username is alphanumeric (with underscores allowed), their email is valid, and that
    their password meets requirements including minimum length, inclusion of digits, uppercase,
    and lowercase letters.

    :ivar username: Username must be alphanumeric with a minimum of 3 characters and a maximum
        of 20 characters. Underscores are allowed.
    :type username: str
    :ivar email: A valid email address.
    :type email: EmailStr
    :ivar password: Password must meet the complexity requirements, including being at least
        8 characters long and containing uppercase, lowercase, and numeric characters.
    :type password: str
    """
    username: str = Field(..., min_length=3, max_length=20, description="Username must be alphanumeric (underscore is allowed)")
    email: EmailStr
    password: str = Field(..., min_length=8, description="Must be at least 8 characters")

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v):
        if not v.replace('_','').isalnum():
            raise ValueError('username must be alphanumeric (underscore is allowed)')
        return v.lower()

    @field_validator('password')
    @classmethod
    def password_complex(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        return v


class UserLogin(BaseModel):
    """
    Represents the data model for user login credentials.

    This class is used to validate and encapsulate user login information, including
    a username or email and password. It enforces constraints on minimum lengths for
    the fields and validates that the username or email is not blank.

    :ivar username_or_email: Represents the username or email for the user. It must
        meet a minimum length requirement and cannot be blank.
    :type username_or_email: str
    :ivar password: Represents the password for the user. It must have at least 8
        characters.
    :type password: str
    """
    username_or_email: str = Field(..., min_length=3, description='Username or email')
    password: str = Field(..., min_length=8, description='Must be at least 8 characters')

    @field_validator('username_or_email')
    @classmethod
    def username_or_email_not_blank(cls, v):
        if not v.strip():
            raise ValueError('Username or email is required')
        return v

class UserPublic(BaseModel):
    """
    Represents a public user with limited access to user details.

    This class serves as a simple data model for representing users in a public
    context, including only essential attributes such as username and email.
    It is built using the BaseModel from Pydantic for data validation and parsing.

    :ivar username: The username of the user.
    :type username: str
    :ivar email: The email address of the user.
    :type email: EmailStr
    """
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserLoginResponse(BaseModel):
    """
    Represents the response returned upon successful user login.

    This class is designed to encapsulate the details of a user's login session,
    including the authentication token, token type, and user public information.
    It provides an organized structure to handle and transport login response data
    within the application.

    :ivar access_token: Token issued to the user upon successful login for
        authentication purposes.
    :type access_token: str
    :ivar token_type: Defines the type of the issued token, typically specifying
        its usage or structure (e.g., "Bearer").
    :type token_type: str
    :ivar user: Public information about the user associated with the login
        session.
    :type user: UserPublic
    """
    access_token: str
    token_type: str
    user: UserPublic