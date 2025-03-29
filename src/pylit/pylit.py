from typing import Any, Dict, Type, TypeVar, get_type_hints

import streamlit as st
from pydantic import BaseModel, Field

T = TypeVar("T", bound=BaseModel)

def get_field_type(field: Any) -> str:
    """Get the type of a Pydantic field."""
    if hasattr(field, "annotation"):
        return str(field.annotation)
    return str(type(field))

def render_field(field_name: str, field: Any, value: Any = None) -> Any:
    """Render a single field based on its type."""
    field_type = get_field_type(field)
    
    if "str" in field_type:
        return st.text_input(field_name, value=value or "")
    elif "int" in field_type:
        return st.number_input(field_name, value=value or 0, step=1)
    elif "float" in field_type:
        return st.number_input(field_name, value=value or 0.0, step=0.1)
    elif "bool" in field_type:
        return st.checkbox(field_name, value=value or False)
    elif "list" in field_type:
        st.write(f"List field: {field_name}")
        return st.text_area(field_name, value=value or "")
    elif "dict" in field_type:
        st.write(f"Dict field: {field_name}")
        return st.text_area(field_name, value=value or "")
    else:
        return st.text_input(field_name, value=value or "")

def pydantic_inputs(model_class: Type[T], title: str = None) -> T:
    """
    Create Streamlit inputs that dynamically generate based on a Pydantic model.
    
    Args:
        model_class: The Pydantic model class to generate inputs from
        title: The title of the section (optional)
    
    Returns:
        An instance of the Pydantic model with the input values
    """
    if title:
        st.subheader(title)
    
    # Get the model fields
    fields = model_class.model_fields
    
    # Create inputs for each field
    form_data: Dict[str, Any] = {}
    
    # Render each field
    for field_name, field in fields.items():
        # Get field description if available
        description = field.description or ""
        
        # Add field label with description if available
        label = f"{field_name}"
        if description:
            label = f"{label} ({description})"
        
        # Render the field
        form_data[field_name] = render_field(label, field)
    
    try:
        # Create and validate the model instance
        instance = model_class(**form_data)
        return instance
    except Exception as e:
        st.error(f"Validation error: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    class UserProfile(BaseModel):
        name: str = Field(description="Your full name")
        age: int = Field(description="Your age")
        email: str = Field(description="Your email address")
        is_active: bool = Field(description="Whether the account is active")
        preferences: Dict[str, str] = Field(description="User preferences")
    
    result = pydantic_inputs(UserProfile, "User Profile Inputs")
    if result:
        st.write("Form Data:", result.model_dump()) 