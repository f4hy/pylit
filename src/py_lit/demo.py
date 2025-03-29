import streamlit as st
from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, conint, confloat

from .py_lit import pydantic_inputs

# Example Pydantic models
class LLMSettings(BaseModel):
    model_name: str = Field(description="Name of the LLM model to use")
    temperature: confloat(ge=0.0, le=2.0) = Field(description="Temperature for sampling (0.0-2.0)")
    max_tokens: conint(ge=1, le=4096) = Field(description="Maximum number of tokens to generate")
    top_p: confloat(ge=0.0, le=1.0) = Field(description="Top-p sampling parameter (0.0-1.0)")
    presence_penalty: confloat(ge=-2.0, le=2.0) = Field(description="Presence penalty (-2.0 to 2.0)")
    frequency_penalty: confloat(ge=-2.0, le=2.0) = Field(description="Frequency penalty (-2.0 to 2.0)")
    stop_sequences: List[str] = Field(description="Stop sequences (comma-separated)")
    system_prompt: str = Field(description="System prompt for the model")

class Product(BaseModel):
    name: str = Field(description="Product name")
    price: confloat(gt=0) = Field(description="Product price (must be positive)")
    description: str = Field(description="Product description")
    tags: List[str] = Field(description="Product tags (comma-separated)")
    in_stock: bool = Field(description="Whether the product is in stock")

class Event(BaseModel):
    title: str = Field(description="Event title")
    date: datetime = Field(description="Event date and time")
    location: str = Field(description="Event location")
    max_participants: Optional[int] = Field(description="Maximum number of participants (optional)")
    description: str = Field(description="Event description")

class Address(BaseModel):
    street: str = Field(description="Street address")
    city: str = Field(description="City")
    state: str = Field(description="State/Province")
    postal_code: str = Field(description="Postal/ZIP code")
    country: str = Field(description="Country")

class Order(BaseModel):
    order_id: str = Field(description="Order ID")
    customer_name: str = Field(description="Customer name")
    items: List[Dict[str, str]] = Field(description="Order items as JSON string")
    shipping_address: Address
    priority: bool = Field(description="Priority shipping")

def main():
    st.set_page_config(page_title="Pylit Automatic Input Generator", layout="wide")
    
    st.title("Pylit Automatic Input Generator")
    st.write("""
    Automatically generate Streamlit inputs from your Pydantic models.
    Each section below demonstrates different model types and their generated inputs.
    """)
    
    # Create columns for different models
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("LLM Settings")
        llm_settings = pydantic_inputs(LLMSettings)
        if llm_settings:
            st.json(llm_settings.model_dump())
        
        st.subheader("Product")
        product = pydantic_inputs(Product)
        if product:
            st.json(product.model_dump())
    
    with col2:
        st.subheader("Event")
        event = pydantic_inputs(Event)
        if event:
            st.json(event.model_dump())
        
        st.subheader("Address")
        address = pydantic_inputs(Address)
        if address:
            st.json(address.model_dump())
    
    # Order form takes full width due to nested Address
    st.subheader("Order")
    order = pydantic_inputs(Order)
    if order:
        st.json(order.model_dump())
    
    # Show all model schemas in a collapsible section
    with st.expander("View Model Schemas"):
        for name, model in [
            ("LLM Settings", LLMSettings),
            ("Product", Product),
            ("Event", Event),
            ("Address", Address),
            ("Order", Order)
        ]:
            st.subheader(f"{name} Schema")
            st.code(model.model_json_schema(), language="json")

if __name__ == "__main__":
    main() 