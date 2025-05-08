# POS-Checkout-System
Online Store Checkout State Machine

This Python application simulates an e-commerce checkout process using a state machine architecture. It guides a user from browsing products to confirming or cancelling an order, handling transitions like payment verification and shipping stages.

FEATURES
--------
- State-driven checkout flow using python-statemachine
- Interactive console input for simulating user behavior
- Handles order rejection based on credit score and purchase amount
- Supports cancel and reject transitions at any stage
- Clear messaging for each transition

STATE FLOW OVERVIEW
--------------------
Browsing
   ↓
 Cart ←→ Add Items
   ↓
Checkout
   ↓
Payment
   ↓
Verification
   ↓
Pending
   ↓
Confirmed
   ↓
Shipped
   ↓
Delivered

Other transitions:
- Any state → Cancelled / Rejected

REQUIREMENTS
-------------
- Python 3.7 or higher
- python-statemachine library

Install it via:
pip install python-statemachine

HOW TO RUN
-----------
1. Clone this repository:
   git clone https://github.com/yourusername/checkout-state-machine.git

   cd checkout-state-machine

3. Run the application:
   python checkout.py

EXAMPLE ACTIONS
----------------
- Add items to the cart with prices
- Input credit score and payment details
- See your order verified, confirmed, shipped, or rejected
- Cancel an order at any point

FILE STRUCTURE
---------------
checkout-state-machine/
│
├── checkout.py      # Main program with state logic and CLI
└── README.txt        # This file

LICENSE
--------
This project is licensed under the MIT License.

ACKNOWLEDGMENTS
----------------
- python-statemachine library by fgmacedo
  https://github.com/fgmacedo/python-statemachine
