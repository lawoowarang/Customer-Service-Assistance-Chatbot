"""
prompts_responses.py
All customer service prompts and their corresponding responses.
Each entry in PROMPTS_AND_RESPONSES is a dict with:
  - 'category': grouping label shown in the prompt panel
  - 'prompt':   the button label / question text
  - 'response': the chatbot reply
"""

COMPANY_NAME = "ShopEase"

WELCOME_MESSAGE = (
    f"Hello! Welcome to {COMPANY_NAME} Support 👋\n\n"
    "I'm here to help you with orders, returns, payments, shipping, and more.\n"
    "Tap a topic below to get started, or scroll to explore all options."
)

PROMPTS_AND_RESPONSES = [
    # ─── ORDERS ───────────────────────────────────────────────────
    {
        "category": "Orders",
        "prompt": "Track my order",
        "response": (
            "📦 To track your order:\n\n"
            "1. Go to My Account → Orders.\n"
            "2. Click the order number you want to track.\n"
            "3. A live tracking link from our courier will appear.\n\n"
            "Alternatively, check the shipping confirmation email — it contains a direct tracking link. "
            "Tracking usually activates within 24 hours of dispatch."
        ),
    },
    {
        "category": "Orders",
        "prompt": "Cancel an order",
        "response": (
            "❌ Order cancellation window:\n\n"
            "• Orders can be cancelled within 1 hour of placing them.\n"
            "• After that, if the order is still 'Processing', contact us immediately.\n"
            "• Once an order is marked 'Dispatched', it can no longer be cancelled — "
            "but you can initiate a return once it arrives.\n\n"
            "To cancel: My Account → Orders → Select order → Cancel Order."
        ),
    },
    {
        "category": "Orders",
        "prompt": "Change order details",
        "response": (
            "✏️ Modifying an order:\n\n"
            "You can change the delivery address or item quantity only while the order "
            "is in 'Processing' status.\n\n"
            "Steps:\n"
            "1. My Account → Orders → Select order → Edit.\n"
            "2. Make your changes and confirm.\n\n"
            "If the Edit button is greyed out, the order has already been handed to our warehouse "
            "and changes are no longer possible. Please contact our live chat for urgent requests."
        ),
    },
    {
        "category": "Orders",
        "prompt": "Order not received",
        "response": (
            "😟 Sorry to hear your order hasn't arrived!\n\n"
            "Please check the following first:\n"
            "• Confirm the expected delivery date in My Account → Orders.\n"
            "• Check if a neighbour or safe place was used by the courier.\n"
            "• Verify the delivery address on your order confirmation.\n\n"
            "If the delivery date has passed and you still have nothing, click "
            "'Report Missing Parcel' on the order page — we'll investigate within 2 business days "
            "and reship or refund at no cost to you."
        ),
    },

    # ─── RETURNS & REFUNDS ────────────────────────────────────────
    {
        "category": "Returns & Refunds",
        "prompt": "How to return an item",
        "response": (
            "🔄 Our return process is simple:\n\n"
            "1. Go to My Account → Orders → Select order → Return Items.\n"
            "2. Choose the item(s) and reason for return.\n"
            "3. Download and print the prepaid return label.\n"
            "4. Pack the item securely in its original packaging if possible.\n"
            "5. Drop it off at any authorised post office or courier point.\n\n"
            "Returns are accepted within 30 days of delivery for most items. "
            "Perishables, personalised items, and digital downloads are non-returnable."
        ),
    },
    {
        "category": "Returns & Refunds",
        "prompt": "Refund status",
        "response": (
            "💰 Refund timeline:\n\n"
            "• Once we receive your returned item, inspection takes 1–2 business days.\n"
            "• Approved refunds are processed within 3–5 business days.\n"
            "• Credit/debit card refunds may take a further 2–5 days to appear, "
            "depending on your bank.\n\n"
            "You can monitor your refund status in My Account → Returns. "
            "You'll also receive an email when the refund is issued."
        ),
    },
    {
        "category": "Returns & Refunds",
        "prompt": "Received wrong item",
        "response": (
            "😮 We apologise for the mix-up!\n\n"
            "Please do the following:\n"
            "1. Take a photo of the item you received and the packaging label.\n"
            "2. Go to My Account → Orders → Report an Issue → Wrong Item.\n"
            "3. Upload the photo and submit.\n\n"
            "We'll arrange a free collection of the wrong item and expedite "
            "the correct one — usually shipped within 24 hours of your report. "
            "No need to repack in the original box."
        ),
    },
    {
        "category": "Returns & Refunds",
        "prompt": "Damaged item received",
        "response": (
            "📷 So sorry about the damaged item!\n\n"
            "Steps to resolve:\n"
            "1. Photograph the damage clearly.\n"
            "2. My Account → Orders → Report an Issue → Damaged Item.\n"
            "3. Attach photos and describe the damage.\n\n"
            "You'll be offered a replacement or a full refund — your choice. "
            "In most cases you won't need to return the damaged item. "
            "Resolution typically happens within 1 business day."
        ),
    },

    # ─── PAYMENTS ─────────────────────────────────────────────────
    {
        "category": "Payments",
        "prompt": "Accepted payment methods",
        "response": (
            "💳 We accept the following payment methods:\n\n"
            "• Visa, Mastercard, American Express\n"
            "• Debit cards\n"
            "• PayPal\n"
            "• Apple Pay & Google Pay\n"
            "• ShopEase Gift Cards\n"
            "• Buy Now Pay Later via Klarna (3 or 6 instalments)\n\n"
            "All transactions are secured with 256-bit SSL encryption. "
            "We do not store your full card details on our servers."
        ),
    },
    {
        "category": "Payments",
        "prompt": "Payment failed",
        "response": (
            "⚠️ Payment failures are usually caused by:\n\n"
            "1. Incorrect card details — double-check the number, expiry, and CVV.\n"
            "2. Insufficient funds or credit limit reached.\n"
            "3. Bank security block — call your bank to authorise the transaction.\n"
            "4. Browser/app issue — try clearing cookies or use a different browser.\n\n"
            "Your cart is saved for 24 hours, so you can retry when the issue is resolved. "
            "If the problem persists, try an alternative payment method or contact us."
        ),
    },
    {
        "category": "Payments",
        "prompt": "Apply a discount code",
        "response": (
            "🏷️ Applying a discount code:\n\n"
            "1. Add items to your cart and proceed to Checkout.\n"
            "2. On the Order Summary page, find the 'Promo Code' field.\n"
            "3. Type or paste your code exactly as given (codes are case-sensitive).\n"
            "4. Click Apply — the discount will show immediately.\n\n"
            "Tips:\n"
            "• Only one code can be used per order.\n"
            "• Codes cannot be applied after payment is complete.\n"
            "• Check the code's expiry date and minimum spend requirements."
        ),
    },
    {
        "category": "Payments",
        "prompt": "Invoice / receipt",
        "response": (
            "🧾 Getting your invoice:\n\n"
            "• A PDF receipt is automatically emailed after every order.\n"
            "• You can also download it anytime: My Account → Orders → Select order → Download Invoice.\n\n"
            "For VAT invoices (business purchases), go to Account Settings → Business Account "
            "and enter your VAT/GST number — future invoices will include it automatically. "
            "For past orders, contact support with your order number and VAT number."
        ),
    },

    # ─── SHIPPING ─────────────────────────────────────────────────
    {
        "category": "Shipping",
        "prompt": "Delivery options & times",
        "response": (
            "🚚 Available delivery options:\n\n"
            "• Standard (3–5 business days) — Free on orders over ₹499\n"
            "• Express (1–2 business days) — ₹99\n"
            "• Same-Day (order before 11 AM) — ₹199, select cities only\n"
            "• International (7–14 business days) — varies by destination\n\n"
            "Delivery times start from the day of dispatch, not the order date. "
            "You'll receive a dispatch notification with your tracking link by email."
        ),
    },
    {
        "category": "Shipping",
        "prompt": "Change delivery address",
        "response": (
            "📍 Changing your delivery address:\n\n"
            "• Before dispatch: Go to My Account → Orders → Edit → Change Address.\n"
            "• After dispatch: Contact our support team immediately. "
            "We may be able to redirect via the courier, but this is not guaranteed.\n\n"
            "To avoid issues in the future, update your default address in "
            "My Account → Address Book before placing your next order."
        ),
    },
    {
        "category": "Shipping",
        "prompt": "International shipping",
        "response": (
            "🌍 International shipping information:\n\n"
            "• We ship to 60+ countries worldwide.\n"
            "• Delivery takes 7–14 business days depending on the destination.\n"
            "• Customs duties and import taxes are the buyer's responsibility "
            "and vary by country.\n\n"
            "To check if we ship to your country, add an item to your cart "
            "and enter your address at checkout — available regions will be shown. "
            "Tracking is available for all international orders."
        ),
    },

    # ─── ACCOUNT ──────────────────────────────────────────────────
    {
        "category": "Account",
        "prompt": "Reset my password",
        "response": (
            "🔐 Resetting your password:\n\n"
            "1. Go to the Login page and click 'Forgot Password?'\n"
            "2. Enter your registered email address.\n"
            "3. Check your inbox for a reset link (valid for 15 minutes).\n"
            "4. Click the link, enter your new password, and confirm.\n\n"
            "Tips:\n"
            "• Check your spam/junk folder if the email doesn't arrive.\n"
            "• Your password must be at least 8 characters with one number.\n"
            "• If your email is no longer accessible, contact support for identity verification."
        ),
    },
    {
        "category": "Account",
        "prompt": "Update account details",
        "response": (
            "👤 Updating your account information:\n\n"
            "Go to My Account → Account Settings to change:\n"
            "• Name and display name\n"
            "• Email address (you'll need to verify the new email)\n"
            "• Phone number\n"
            "• Saved addresses\n"
            "• Communication preferences\n\n"
            "For security, changes to your email or phone number trigger a "
            "verification step. If you're having trouble, please contact our support team."
        ),
    },
    {
        "category": "Account",
        "prompt": "Delete my account",
        "response": (
            "🗑️ Requesting account deletion:\n\n"
            "We're sorry to see you go. To delete your account:\n\n"
            "1. Go to My Account → Account Settings → Scroll to the bottom.\n"
            "2. Click 'Delete Account' and follow the prompts.\n"
            "3. Your account will be scheduled for deletion in 30 days.\n\n"
            "During this period you can log back in to cancel the deletion. "
            "After 30 days, all personal data is permanently removed. "
            "Note: Active orders must be fulfilled or cancelled first."
        ),
    },

    # ─── PRODUCTS ─────────────────────────────────────────────────
    {
        "category": "Products",
        "prompt": "Product availability",
        "response": (
            "🔍 Checking product availability:\n\n"
            "• Live stock levels are shown on each product page.\n"
            "• If an item shows 'Out of Stock', click 'Notify Me' — "
            "you'll get an email the moment it's back.\n\n"
            "Stock levels update in real time, so availability can change quickly "
            "during sales. Adding to cart does not reserve stock; only completing "
            "checkout guarantees your item."
        ),
    },
    {
        "category": "Products",
        "prompt": "Product warranty",
        "response": (
            "🛡️ Warranty information:\n\n"
            "• Electronics: 1 year manufacturer warranty by default.\n"
            "• Appliances: 1–2 years depending on the brand.\n"
            "• Clothing & accessories: 30-day quality guarantee.\n"
            "• ShopEase Extended Warranty: available at checkout for eligible items, "
            "extending coverage up to 3 years.\n\n"
            "To make a warranty claim: My Account → Orders → Select item → Warranty Claim. "
            "Keep your proof of purchase — it's needed for all claims."
        ),
    },
    {
        "category": "Products",
        "prompt": "Compare products",
        "response": (
            "📊 How to compare products:\n\n"
            "1. On any category or search results page, tick the 'Compare' checkbox "
            "on up to 4 products.\n"
            "2. Click the 'Compare Selected' button that appears at the bottom of the screen.\n"
            "3. A side-by-side spec table will open showing all key features.\n\n"
            "You can also find curated comparison guides in our Blog & Buying Guides section "
            "for popular categories like laptops, smartphones, and appliances."
        ),
    },

    # ─── LOYALTY & OFFERS ─────────────────────────────────────────
    {
        "category": "Offers & Loyalty",
        "prompt": "Loyalty points balance",
        "response": (
            "⭐ Checking your loyalty points:\n\n"
            "• Go to My Account → Rewards to see your current balance.\n"
            "• You earn 1 point for every ₹10 spent.\n"
            "• 100 points = ₹10 off your next order.\n\n"
            "Points are credited 48 hours after delivery confirmation. "
            "They expire after 12 months of account inactivity. "
            "You can redeem points at checkout in the 'Use Rewards' section."
        ),
    },
    {
        "category": "Offers & Loyalty",
        "prompt": "Current sale offers",
        "response": (
            "🎉 How to find active deals:\n\n"
            "• Visit the Deals & Offers page — updated daily.\n"
            "• Filter by category, brand, or discount percentage.\n"
            "• Subscribe to our newsletter (Account Settings → Notifications) "
            "for exclusive early-access offers.\n\n"
            "Flash sales run for limited hours — turn on sale alerts in the app "
            "so you never miss them. Members of ShopEase Plus get an extra 5% off all sale items."
        ),
    },
    {
        "category": "Offers & Loyalty",
        "prompt": "Refer a friend",
        "response": (
            "👫 ShopEase Referral Programme:\n\n"
            "• Get your unique referral link from My Account → Refer & Earn.\n"
            "• Share it with friends — they receive ₹150 off their first order.\n"
            "• You earn ₹150 in store credit once they complete their first purchase.\n\n"
            "There's no limit on referrals! Credits are added to your account "
            "within 7 days of your friend's first order and are valid for 6 months."
        ),
    },

    # ─── CONTACT ──────────────────────────────────────────────────
    {
        "category": "Contact Us",
        "prompt": "Live chat support",
        "response": (
            "💬 Live chat is available:\n\n"
            "• Monday – Saturday: 9:00 AM – 9:00 PM\n"
            "• Sunday: 10:00 AM – 6:00 PM\n\n"
            "To start a chat, click the chat icon in the bottom-right corner of our website. "
            "Average wait time is under 2 minutes. For complex issues, "
            "have your order number ready to speed things up."
        ),
    },
    {
        "category": "Contact Us",
        "prompt": "Email support",
        "response": (
            "📧 Email us at support@shopease.com\n\n"
            "We aim to reply within:\n"
            "• Standard queries: 24 hours\n"
            "• Order/refund issues: 12 hours\n"
            "• Urgent/escalated cases: 4 hours\n\n"
            "Please include your order number, registered email, and a brief description "
            "of your issue so we can resolve it faster. "
            "You'll receive an auto-acknowledgement immediately with a ticket number."
        ),
    },
    {
        "category": "Contact Us",
        "prompt": "Call support",
        "response": (
            "📞 Phone support:\n\n"
            "Toll-Free: 1800-123-4567\n"
            "Hours: Monday – Saturday, 9:00 AM – 7:00 PM\n\n"
            "• Press 1 for Orders & Delivery\n"
            "• Press 2 for Returns & Refunds\n"
            "• Press 3 for Payments\n"
            "• Press 0 to speak with an agent directly\n\n"
            "Average hold time is under 5 minutes. "
            "Calls may be recorded for quality and training purposes."
        ),
    },
]
