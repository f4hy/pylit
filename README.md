# streamdantic - Automatic Input Generator

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Dependencies](https://img.shields.io/badge/dependencies-pydantic%20%7C%20streamlit-blue.svg)](https://github.com/f4hy/streamdantic/blob/main/pyproject.toml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A Python package that automatically generates Streamlit inputs from your Pydantic models. streamdantic makes it easy to create interactive web forms that validate input against your Pydantic schemas, with zero additional code.

## Features

- Automatically generates Streamlit inputs from Pydantic models
- Real-time validation as you type
- Supports various field types:
  - Strings (text input)
  - Numbers (with constraints)
  - Booleans (checkbox)
  - Lists (text area)
  - Dictionaries (text area)
  - Nested models
  - Optional fields
- Field descriptions and validation messages
- JSON schema visualization
- Example models included

## Installation

This project uses `uv` for package management. Make sure you have `uv` installed first:

```bash
pip install uv
```

Then install the package in development mode:

```bash
uv pip install -e .
```

## Running the Demo

To run the demo application:

```bash
streamlit run run_demo.py
```

The demo showcases various model types:
- LLM Settings (with constrained fields)
- Product (with nested lists)
- Event (with datetime)
- Address (simple form)
- Order (with nested Address model)

## Example Usage

```python
import streamlit as st
from pydantic import BaseModel, Field
from pylit import pydantic_inputs

# Define your Pydantic model
class MyModel(BaseModel):
    name: str = Field(description="Enter your name")
    age: int = Field(description="Enter your age")
    is_active: bool = Field(description="Whether the account is active")

# Create the inputs
result = pydantic_inputs(MyModel)
if result:
    st.write("Input values:", result.model_dump())
```

## Supported Field Types

- Strings (text input)
- Integers (number input)
- Floats (number input with decimal steps)
- Booleans (checkbox)
- Lists (text area)
- Dictionaries (text area)
- Datetime
- Optional fields
- Constrained types (conint, confloat)
- Nested models

## Development

This project uses:
- [Black](https://github.com/psf/black) for code formatting
- [Ruff](https://github.com/astral-sh/ruff) for linting
- [Pydantic](https://github.com/pydantic/pydantic) for data validation
- [Streamlit](https://github.com/streamlit/streamlit) for the UI

## License

Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
