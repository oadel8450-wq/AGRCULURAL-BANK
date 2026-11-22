# -*- coding: utf-8 -*-

import math

from kivy.app import App
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, RoundedRectangle, Rectangle


# ============================================================
# COLORS
# ============================================================

NAVY = (0.035, 0.10, 0.20, 1)
BLUE = (0.05, 0.28, 0.55, 1)
BLUE2 = (0.08, 0.40, 0.72, 1)

GREEN = (0.08, 0.48, 0.25, 1)
GREEN2 = (0.12, 0.65, 0.32, 1)

RED = (0.82, 0.08, 0.10, 1)
ORANGE = (0.95, 0.48, 0.08, 1)
GOLD = (0.95, 0.72, 0.15, 1)

WHITE = (1, 1, 1, 1)
LIGHT = (0.92, 0.95, 0.98, 1)
GRAY = (0.65, 0.70, 0.76, 1)
DARK = (0.08, 0.10, 0.13, 1)


# ============================================================
# AGRICULTURAL DATA
# ============================================================

CROPS = {
    "Wheat": 18000,
    "Corn": 18000,
    "Rice": 18000,
    "Beans": 18000,
    "Clover": 18000,
    "Cotton": 18000,

    "Tomato": 39000,
    "Potato": 39000,
    "Vegetables": 39000,
    "Gardens": 39000,
    "Fruit": 39000,
}


# ============================================================
# DEFAULT SETTINGS
# ALL CAN BE CHANGED FROM SETTINGS SCREEN
# ============================================================

CERTIFICATE_RATES = [
    "17%",
    "18%",
    "19%",
    "20%"
]

FINANCE_OPTIONS = [
    "80%",
    "90%"
]

EMPLOYEE_RATES = [
    "14%",
    "15%",
    "16%",
    "18%",
    "19%",
    "20%",
    "25%"
]

# Employee loan maximum deduction from salary
EMPLOYEE_DEDUCTION_PERCENT = 50.0

# Extra rate for certificate-backed loan
LOAN_EXTRA_RATE = 2.5


# ============================================================
# HELPERS
# ============================================================

def money(value):
    try:
        return "{:,.2f}".format(float(value))
    except Exception:
        return "0.00"


def percent_number(text):
    try:
        return float(str(text).replace("%", "").strip())
    except Exception:
        return 0.0


def make_label(
    text="",
    size=16,
    color=WHITE,
    bold=False,
    halign="left",
    valign="middle"
):
    lbl = Label(
        text=str(text),
        font_size=dp(size),
        color=color,
        bold=bold,
        halign=halign,
        valign=valign,
    )

    lbl.text_size = (None, None)

    return lbl


# ============================================================
# CARD
# ============================================================

class Card(BoxLayout):

    def __init__(
        self,
        bg=BLUE,
        radius=16,
        **kwargs
    ):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*bg)

            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(radius)]
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# ============================================================
# BUTTON
# ============================================================

class AppButton(Button):

    def __init__(
        self,
        bg=GREEN,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = bg

        self.color = WHITE
        self.bold = True
        self.font_size = dp(15)

        self.padding = [
            dp(8),
            dp(5)
        ]


# ============================================================
# HEADER
# ============================================================

class Header(BoxLayout):

    def __init__(
        self,
        title,
        icon="●",
        **kwargs
    ):

        super().__init__(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(72),
            padding=[
                dp(15),
                dp(8)
            ],
            spacing=dp(12),
            **kwargs
        )

        with self.canvas.before:
            Color(*RED)

            self.rect = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

        icon_box = Card(
            bg=GREEN,
            orientation="vertical",
            size_hint_x=None,
            width=dp(55),
        )

        icon_box.add_widget(
            make_label(
                icon,
                size=25,
                color=WHITE,
                bold=True,
                halign="center"
            )
        )

        self.add_widget(icon_box)

        title_box = BoxLayout(
            orientation="vertical",
            padding=[dp(2), 0]
        )

        title_box.add_widget(
            make_label(
                title,
                size=20,
                color=WHITE,
                bold=True
            )
        )

        title_box.add_widget(
            make_label(
                "Egyptian Agricultural Bank",
                size=11,
                color=WHITE
            )
        )

        self.add_widget(title_box)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# ============================================================
# BASE SCREEN
# ============================================================

class BaseScreen(Screen):

    title = ""
    icon = "●"

    def build_base(self):

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(8)
        )

        root.add_widget(
            Header(
                self.title,
                self.icon
            )
        )

        body = BoxLayout(
            orientation="vertical",
            padding=[
                dp(10),
                dp(8)
            ],
            spacing=dp(8)
        )

        root.add_widget(body)

        footer = Label(
            text=(
                "Adel Omer Abdel Aziz  |  "
                "Ashmant Branch  |  "
                "Beni Suef Sector  |  "
                "Program Developer"
            ),
            font_size=dp(9),
            color=GRAY,
            size_hint_y=None,
            height=dp(25),
            halign="center",
            valign="middle"
        )

        root.add_widget(footer)

        self.add_widget(root)

        return body


# ============================================================
# HOME
# ============================================================

class HomeScreen(BaseScreen):

    title = "Banking Services"
    icon = "★"

    def on_enter(self):

        if self.children:
            return

        body = self.build_base()

        title = make_label(
            "Select a Service",
            size=18,
            color=GOLD,
            bold=True,
            halign="center"
        )

        title.size_hint_y = None
        title.height = dp(35)

        body.add_widget(title)

        grid = GridLayout(
            cols=2,
            spacing=dp(10),
            padding=[dp(5), dp(5)]
        )

        services = [
            (
                "🌿\nAgricultural\nLoans",
                GREEN,
                "agricultural"
            ),

            (
                "★\nCertificates",
                BLUE2,
                "certificates"
            ),

            (
                "👤\nEmployee\nLoans",
                GREEN2,
                "employee"
            ),

            (
                "!\nLate\nCustomers",
                RED,
                "late"
            ),

            (
                "⚙\nSettings",
                NAVY,
                "settings"
            ),

            (
                "×\nExit",
                ORANGE,
                "exit"
            ),
        ]

        for text, color, action in services:

            btn = AppButton(
                text=text,
                bg=color,
                font_size=dp(15)
            )

            if action == "agricultural":
                btn.bind(
                    on_release=self.open_agricultural
                )

            elif action == "certificates":
                btn.bind(
                    on_release=self.open_certificates
                )

            elif action == "employee":
                btn.bind(
                    on_release=self.open_employee
                )

            elif action == "late":
                btn.bind(
                    on_release=self.open_late
                )

            elif action == "settings":
                btn.bind(
                    on_release=self.open_settings
                )

            elif action == "exit":
                btn.bind(
                    on_release=self.exit_app
                )

            grid.add_widget(btn)

        body.add_widget(grid)

        info = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(85)
        )

        info.add_widget(
            make_label(
                "Professional banking calculator",
                size=14,
                color=WHITE,
                bold=True,
                halign="center"
            )
        )

        info.add_widget(
            make_label(
                "Loans • Certificates • Employee Loans • Customer Follow-up",
                size=10,
                color=GRAY,
                halign="center"
            )
        )

        body.add_widget(info)

    def open_agricultural(self, *args):
        self.manager.current = "agricultural"

    def open_certificates(self, *args):
        self.manager.current = "certificates"

    def open_employee(self, *args):
        self.manager.current = "employee"

    def open_late(self, *args):
        self.manager.current = "late"

    def open_settings(self, *args):
        self.manager.current = "settings"

    def exit_app(self, *args):
        App.get_running_app().stop()


# ============================================================
# AGRICULTURAL LOANS
# ============================================================

class AgriculturalScreen(BaseScreen):

    title = "Agricultural Loans"
    icon = "🌿"

    def on_enter(self):

        if self.children:
            return

        body = self.build_base()

        scroll = ScrollView(
            do_scroll_x=False
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=[dp(2), dp(2)],
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        customer_card = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        customer_card.add_widget(
            make_label(
                "Customer Name",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.ag_customer = TextInput(
            hint_text="Enter customer name",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        customer_card.add_widget(
            self.ag_customer
        )

        content.add_widget(
            customer_card
        )

        crop_card = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(100)
        )

        crop_card.add_widget(
            make_label(
                "Crop / Activity",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.crop_spinner = Spinner(
            text="Select Crop",
            values=list(CROPS.keys()),
            font_size=dp(14),
            background_normal="",
            background_color=GREEN,
            color=WHITE
        )

        self.crop_spinner.bind(
            text=self.crop_changed
        )

        crop_card.add_widget(
            self.crop_spinner
        )

        self.crop_rate = make_label(
            "Category Rate: -",
            size=12,
            color=GOLD
        )

        crop_card.add_widget(
            self.crop_rate
        )

        content.add_widget(
            crop_card
        )

        area_card = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(145)
        )

        area_card.add_widget(
            make_label(
                "Cultivated Area",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        row = BoxLayout(
            spacing=dp(8),
            size_hint_y=None,
            height=dp(48)
        )

        self.feddan_input = TextInput(
            hint_text="Feddan",
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        self.qirat_input = TextInput(
            hint_text="Qirat",
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        row.add_widget(
            self.feddan_input
        )

        row.add_widget(
            self.qirat_input
        )

        area_card.add_widget(row)

        area_card.add_widget(
            make_label(
                "1 Feddan = 24 Qirat",
                size=11,
                color=GRAY,
                halign="center"
            )
        )

        content.add_widget(
            area_card
        )

        calc_btn = AppButton(
            text="CALCULATE AGRICULTURAL LOAN",
            bg=GREEN2,
            size_hint_y=None,
            height=dp(50)
        )

        calc_btn.bind(
            on_release=self.calculate_agricultural
        )

        content.add_widget(
            calc_btn
        )

        result = Card(
            bg=DARK,
            orientation="vertical",
            padding=[
                dp(12),
                dp(10)
            ],
            spacing=dp(5),
            size_hint_y=None,
            height=dp(155)
        )

        result.add_widget(
            make_label(
                "LOAN RESULT",
                size=16,
                color=GOLD,
                bold=True,
                halign="center"
            )
        )

        self.ag_result = make_label(
            "Enter the customer, crop and cultivated area.",
            size=13,
            color=WHITE,
            halign="center"
        )

        result.add_widget(
            self.ag_result
        )

        content.add_widget(
            result
        )

        back = AppButton(
            text="← BACK TO SERVICES",
            bg=BLUE,
            size_hint_y=None,
            height=dp(45)
        )

        back.bind(
            on_release=lambda x: self.back_home()
        )

        content.add_widget(back)

        scroll.add_widget(content)

        body.add_widget(scroll)

    def crop_changed(self, spinner, text):

        if text in CROPS:

            self.crop_rate.text = (
                "Category Rate: "
                + money(CROPS[text])
                + " EGP / Feddan"
            )

        else:
            self.crop_rate.text = "Category Rate: -"

    def calculate_agricultural(self, *args):

        try:

            crop = self.crop_spinner.text

            if crop not in CROPS:

                self.ag_result.text = (
                    "Please select a crop."
                )

                return

            feddan = float(
                self.feddan_input.text or 0
            )

            qirat = float(
                self.qirat_input.text or 0
            )

            if feddan < 0 or qirat < 0:
                raise ValueError

            total_area = (
                feddan +
                (qirat / 24.0)
            )

            rate = CROPS[crop]

            loan = (
                total_area *
                rate
            )

            self.ag_result.text = (
                "Customer: "
                + (
                    self.ag_customer.text.strip()
                    or "Not specified"
                )

                + "\n\nCrop: "
                + crop

                + "\nArea: "
                + "{:.2f}".format(total_area)
                + " Feddan"

                + "\nRate: "
                + money(rate)
                + " EGP / Feddan"

                + "\n\nTOTAL LOAN: "
                + money(loan)
                + " EGP"
            )

        except Exception:

            self.ag_result.text = (
                "Please enter valid numbers for "
                "Feddan and Qirat."
            )

    def back_home(self):
        self.manager.current = "home"


# ============================================================
# CERTIFICATES
# ============================================================

class CertificateScreen(BaseScreen):

    title = "Certificates & Certificate Loan"
    icon = "★"

    def on_enter(self):

        if self.children:
            return

        body = self.build_base()

        scroll = ScrollView(
            do_scroll_x=False
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=[dp(2), dp(2)],
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        card1 = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(78)
        )

        card1.add_widget(
            make_label(
                "1. Customer Name",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.cert_customer = TextInput(
            hint_text="Enter customer name",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        card1.add_widget(
            self.cert_customer
        )

        content.add_widget(card1)

        card2 = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(78)
        )

        card2.add_widget(
            make_label(
                "2. Certificate Amount (EGP)",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.cert_amount = TextInput(
            hint_text="Example: 100000",
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        card2.add_widget(
            self.cert_amount
        )

        content.add_widget(card2)

        card3 = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(125)
        )

        row = BoxLayout(
            spacing=dp(8)
        )

        rate_box = BoxLayout(
            orientation="vertical"
        )

        rate_box.add_widget(
            make_label(
                "Certificate Rate",
                size=12,
                color=GOLD,
                bold=True
            )
        )

        self.cert_rate = Spinner(
            text="17%",
            values=CERTIFICATE_RATES,
            background_normal="",
            background_color=GREEN,
            color=WHITE,
            font_size=dp(14)
        )

        rate_box.add_widget(
            self.cert_rate
        )

        finance_box = BoxLayout(
            orientation="vertical"
        )

        finance_box.add_widget(
            make_label(
                "Loan Finance %",
                size=12,
                color=GOLD,
                bold=True
            )
        )

        self.finance_percent = Spinner(
            text="90%",
            values=FINANCE_OPTIONS,
            background_normal="",
            background_color=BLUE2,
            color=WHITE,
            font_size=dp(14)
        )

        finance_box.add_widget(
            self.finance_percent
        )

        row.add_widget(rate_box)
        row.add_widget(finance_box)

        card3.add_widget(row)

        content.add_widget(card3)

        calculate = AppButton(
            text="CALCULATE CERTIFICATE COMPARISON",
            bg=GREEN2,
            size_hint_y=None,
            height=dp(50)
        )

        calculate.bind(
            on_release=self.calculate_certificate
        )

        content.add_widget(calculate)

        result = Card(
            bg=DARK,
            orientation="vertical",
            padding=[
                dp(10),
                dp(8)
            ],
            spacing=dp(3),
            size_hint_y=None,
            height=dp(570)
        )

        result.add_widget(
            make_label(
                "CERTIFICATE LOAN RESULTS",
                size=16,
                color=GOLD,
                bold=True,
                halign="center"
            )
        )

        self.cert_result = make_label(
            "Enter certificate amount.",
            size=12,
            color=WHITE,
            halign="left"
        )

        result.add_widget(
            self.cert_result
        )

        content.add_widget(result)

        back = AppButton(
            text="← BACK TO SERVICES",
            bg=BLUE2,
            size_hint_y=None,
            height=dp(45)
        )

        back.bind(
            on_release=lambda x: self.back_home()
        )

        content.add_widget(back)

        scroll.add_widget(content)

        body.add_widget(scroll)

    def calculate_payment(
        self,
        principal,
        annual_rate,
        months
    ):

        if principal <= 0 or months <= 0:
            return 0

        monthly_rate = (
            annual_rate /
            100.0 /
            12.0
        )

        if monthly_rate == 0:
            return principal / months

        factor = (
            (1 + monthly_rate)
            ** months
        )

        payment = (
            principal
            * monthly_rate
            * factor
            /
            (factor - 1)
        )

        return payment

    def certificate_case(
        self,
        amount,
        finance,
        cert_rate,
        years
    ):

        months = int(
            round(years * 12)
        )

        loan_amount = (
            amount *
            finance /
            100.0
        )

        loan_rate = (
            cert_rate +
            LOAN_EXTRA_RATE
        )

        monthly_payment = (
            self.calculate_payment(
                loan_amount,
                loan_rate,
                months
            )
        )

        total_paid = (
            monthly_payment *
            months
        )

        return (
            loan_amount,
            loan_rate,
            monthly_payment,
            total_paid
        )

    def calculate_certificate(self, *args):

        try:

            amount = float(
                self.cert_amount.text or 0
            )

            if amount <= 0:
                raise ValueError

            cert_rate = percent_number(
                self.cert_rate.text
            )

            finance_selected = percent_number(
                self.finance_percent.text
            )

            annual_return = (
                amount *
                cert_rate /
                100
            )

            monthly_return = (
                annual_return /
                12
            )

            result_text = (
                "Customer: "
                + (
                    self.cert_customer.text.strip()
                    or "Not specified"
                )

                + "\n\nCERTIFICATE"
                + "\nCertificate Amount: "
                + money(amount)
                + " EGP"

                + "\nCertificate Rate: "
                + money(cert_rate)
                + "%"

                + "\nAnnual Return: "
                + money(annual_return)
                + " EGP"

                + "\nMonthly Return: "
                + money(monthly_return)
                + " EGP"

                + "\n\n"
                + "=" * 32

                + "\nSELECTED FINANCE: "
                + money(finance_selected)
                + "%"
            )

            # ------------------------------------------------
            # SELECTED FINANCE
            # ------------------------------------------------

            result_text += (
                "\n\nAMOUNT RECEIVED BY CUSTOMER"
                + "\n"
                + money(
                    amount *
                    finance_selected /
                    100
                )
                + " EGP"
            )

            for years in [3, 5, 10]:

                loan_amount, loan_rate, payment, total = (
                    self.certificate_case(
                        amount,
                        finance_selected,
                        cert_rate,
                        years
                    )
                )

                result_text += (
                    "\n\n--- "
                    + str(years)
                    + " YEARS ---"

                    + "\nCustomer receives: "
                    + money(loan_amount)
                    + " EGP"

                    + "\nLoan rate: "
                    + money(loan_rate)
                    + "%"

                    + "\nMonthly installment: "
                    + money(payment)
                    + " EGP"

                    + "\nTotal repayment: "
                    + money(total)
                    + " EGP"
                )

            # ------------------------------------------------
            # COMPARISON 80% / 90%
            # ------------------------------------------------

            result_text += (
                "\n\n"
                + "=" * 32
                + "\n80% VS 90% COMPARISON"
            )

            for finance in [80, 90]:

                result_text += (
                    "\n\nFINANCE "
                    + str(finance)
                    + "%"
                    + "\nCustomer receives: "
                    + money(
                        amount *
                        finance /
                        100
                    )
                    + " EGP"
                )

                for years in [3, 5, 10]:

                    loan_amount, loan_rate, payment, total = (
                        self.certificate_case(
                            amount,
                            finance,
                            cert_rate,
                            years
                        )
                    )

                    result_text += (
                        "\n"
                        + str(years)
                        + " Years → "
                        + money(payment)
                        + " EGP / month"
                    )

            self.cert_result.text = result_text

        except Exception:

            self.cert_result.text = (
                "Please enter a valid "
                "certificate amount."
            )

    def back_home(self):
        self.manager.current = "home"


# ============================================================
# EMPLOYEE LOANS
# ============================================================

class EmployeeLoanScreen(BaseScreen):

    title = "Employee Loans"
    icon = "👤"

    def on_enter(self):

        if self.children:
            return

        body = self.build_base()

        scroll = ScrollView(
            do_scroll_x=False
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(9),
            padding=[dp(2), dp(2)],
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        # Salary
        salary_card = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        salary_card.add_widget(
            make_label(
                "Employee Monthly Salary (EGP)",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.employee_salary = TextInput(
            hint_text="Example: 10000",
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        salary_card.add_widget(
            self.employee_salary
        )

        content.add_widget(
            salary_card
        )

        # Years
        years_card = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        years_card.add_widget(
            make_label(
                "Years Remaining Until Retirement",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.retirement_years = TextInput(
            hint_text="Example: 5",
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        years_card.add_widget(
            self.retirement_years
        )

        content.add_widget(
            years_card
        )

        # Rate
        rate_card = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(85)
        )

        rate_card.add_widget(
            make_label(
                "Employee Loan Interest Rate",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.employee_rate = Spinner(
            text=EMPLOYEE_RATES[0],
            values=EMPLOYEE_RATES,
            background_normal="",
            background_color=GREEN,
            color=WHITE,
            font_size=dp(14)
        )

        rate_card.add_widget(
            self.employee_rate
        )

        content.add_widget(
            rate_card
        )

        # Deduction
        deduction_card = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(10),
                dp(7)
            ],
            size_hint_y=None,
            height=dp(90)
        )

        deduction_card.add_widget(
            make_label(
                "Maximum Salary Deduction %",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.employee_deduction = TextInput(
            text=str(
                EMPLOYEE_DEDUCTION_PERCENT
            ),
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        deduction_card.add_widget(
            self.employee_deduction
        )

        content.add_widget(
            deduction_card
        )

        calculate = AppButton(
            text="CALCULATE EMPLOYEE LOAN",
            bg=GREEN2,
            size_hint_y=None,
            height=dp(50)
        )

        calculate.bind(
            on_release=self.calculate_employee
        )

        content.add_widget(
            calculate
        )

        result = Card(
            bg=DARK,
            orientation="vertical",
            padding=[
                dp(10),
                dp(8)
            ],
            spacing=dp(4),
            size_hint_y=None,
            height=dp(430)
        )

        result.add_widget(
            make_label(
                "EMPLOYEE LOAN RESULT",
                size=16,
                color=GOLD,
                bold=True,
                halign="center"
            )
        )

        self.employee_result = make_label(
            "Enter salary and years until retirement.",
            size=12,
            color=WHITE,
            halign="left"
        )

        result.add_widget(
            self.employee_result
        )

        content.add_widget(result)

        back = AppButton(
            text="← BACK TO SERVICES",
            bg=BLUE2,
            size_hint_y=None,
            height=dp(45)
        )

        back.bind(
            on_release=lambda x: self.back_home()
        )

        content.add_widget(back)

        scroll.add_widget(content)

        body.add_widget(scroll)

    def calculate_employee_payment(
        self,
        principal,
        annual_rate,
        months
    ):

        if principal <= 0 or months <= 0:
            return 0

        monthly_rate = (
            annual_rate /
            100 /
            12
        )

        if monthly_rate == 0:
            return principal / months

        factor = (
            1 +
            monthly_rate
        ) ** months

        return (
            principal *
            monthly_rate *
            factor /
            (factor - 1)
        )

    def calculate_max_loan(
        self,
        monthly_payment,
        annual_rate,
        months
    ):

        if (
            monthly_payment <= 0
            or months <= 0
        ):
            return 0

        monthly_rate = (
            annual_rate /
            100 /
            12
        )

        if monthly_rate == 0:
            return (
                monthly_payment *
                months
            )

        factor = (
            1 +
            monthly_rate
        ) ** (-months)

        principal = (
            monthly_payment *
            (1 - factor) /
            monthly_rate
        )

        return principal

    def calculate_employee(self, *args):

        try:

            salary = float(
                self.employee_salary.text or 0
            )

            years = float(
                self.retirement_years.text or 0
            )

            deduction = float(
                self.employee_deduction.text or 0
            )

            rate = percent_number(
                self.employee_rate.text
            )

            if (
                salary <= 0
                or years <= 0
                or deduction <= 0
                or deduction > 100
            ):
                raise ValueError

            months = int(
                round(years * 12)
            )

            max_installment = (
                salary *
                deduction /
                100
            )

            max_loan = (
                self.calculate_max_loan(
                    max_installment,
                    rate,
                    months
                )
            )

            total_paid = (
                max_installment *
                months
            )

            interest_cost = (
                total_paid -
                max_loan
            )

            self.employee_result.text = (

                "EMPLOYEE LOAN"

                + "\n\nSalary: "
                + money(salary)
                + " EGP"

                + "\nAllowed deduction: "
                + money(deduction)
                + "%"

                + "\nMaximum monthly installment: "
                + money(max_installment)
                + " EGP"

                + "\n\nRemaining until retirement: "
                + "{:.0f}".format(years)
                + " Years"

                + "\nNumber of months: "
                + str(months)

                + "\n\nInterest rate: "
                + money(rate)
                + "%"

                + "\n\nMAXIMUM LOAN AMOUNT:"
                + "\n"
                + money(max_loan)
                + " EGP"

                + "\n\nMonthly installment:"
                + "\n"
                + money(max_installment)
                + " EGP"

                + "\n\nTotal repayment:"
                + "\n"
                + money(total_paid)
                + " EGP"

                + "\n\nEstimated interest:"
                + "\n"
                + money(interest_cost)
                + " EGP"
            )

        except Exception:

            self.employee_result.text = (
                "Please enter valid employee "
                "salary, retirement years "
                "and deduction percentage."
            )

    def back_home(self):
        self.manager.current = "home"


# ============================================================
# SETTINGS
# ============================================================

class SettingsScreen(BaseScreen):

    title = "Loan Settings"
    icon = "⚙"

    def on_enter(self):

        if self.children:
            return

        body = self.build_base()

        scroll = ScrollView(
            do_scroll_x=False
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=[dp(3), dp(3)],
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        info = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(85)
        )

        info.add_widget(
            make_label(
                "Editable Banking Settings",
                size=16,
                color=GOLD,
                bold=True,
                halign="center"
            )
        )

        info.add_widget(
            make_label(
                "Change the values below whenever the bank rules change.",
                size=11,
                color=GRAY,
                halign="center"
            )
        )

        content.add_widget(info)

        # Employee deduction
        card1 = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=100
        )

        card1.add_widget(
            make_label(
                "Employee Maximum Deduction %",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.setting_deduction = TextInput(
            text=str(
                EMPLOYEE_DEDUCTION_PERCENT
            ),
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        card1.add_widget(
            self.setting_deduction
        )

        content.add_widget(card1)

        # Employee rates
        card2 = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=180
        )

        card2.add_widget(
            make_label(
                "Employee Loan Interest Rates",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.setting_employee_rates = TextInput(
            text=", ".join(
                EMPLOYEE_RATES
            ),
            multiline=True,
            font_size=dp(13),
            background_color=WHITE,
            foreground_color=DARK
        )

        card2.add_widget(
            self.setting_employee_rates
        )

        content.add_widget(card2)

        # Certificate rates
        card3 = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=180
        )

        card3.add_widget(
            make_label(
                "Certificate Rates",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.setting_certificate_rates = TextInput(
            text=", ".join(
                CERTIFICATE_RATES
            ),
            multiline=True,
            font_size=dp(13),
            background_color=WHITE,
            foreground_color=DARK
        )

        card3.add_widget(
            self.setting_certificate_rates
        )

        content.add_widget(card3)

        # Extra rate
        card4 = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=100
        )

        card4.add_widget(
            make_label(
                "Certificate Loan Extra Rate %",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.setting_extra_rate = TextInput(
            text=str(
                LOAN_EXTRA_RATE
            ),
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        card4.add_widget(
            self.setting_extra_rate
        )

        content.add_widget(card4)

        save = AppButton(
            text="SAVE SETTINGS",
            bg=GREEN2,
            size_hint_y=None,
            height=dp(50)
        )

        save.bind(
            on_release=self.save_settings
        )

        content.add_widget(save)

        self.settings_result = make_label(
            "",
            size=13,
            color=GOLD,
            halign="center"
        )

        self.settings_result.size_hint_y = None
        self.settings_result.height = dp(45)

        content.add_widget(
            self.settings_result
        )

        back = AppButton(
            text="← BACK TO SERVICES",
            bg=BLUE2,
            size_hint_y=None,
            height=dp(45)
        )

        back.bind(
            on_release=lambda x: self.back_home()
        )

        content.add_widget(back)

        scroll.add_widget(content)

        body.add_widget(scroll)

    def save_settings(self, *args):

        global EMPLOYEE_DEDUCTION_PERCENT
        global EMPLOYEE_RATES
        global CERTIFICATE_RATES
        global LOAN_EXTRA_RATE

        try:

            deduction = float(
                self.setting_deduction.text
            )

            if deduction <= 0 or deduction > 100:
                raise ValueError

            raw_employee = (
                self.setting_employee_rates.text
            )

            employee_rates = []

            for item in raw_employee.split(","):

                item = item.strip()

                if item:

                    number = float(
                        item.replace("%", "")
                    )

                    if number <= 0:
                        continue

                    employee_rates.append(
                        "{:g}%".format(number)
                    )

            if not employee_rates:
                raise ValueError

            raw_certificate = (
                self.setting_certificate_rates.text
            )

            certificate_rates = []

            for item in raw_certificate.split(","):

                item = item.strip()

                if item:

                    number = float(
                        item.replace("%", "")
                    )

                    if number <= 0:
                        continue

                    certificate_rates.append(
                        "{:g}%".format(number)
                    )

            if not certificate_rates:
                raise ValueError

            extra = float(
                self.setting_extra_rate.text
            )

            if extra < 0:
                raise ValueError

            EMPLOYEE_DEDUCTION_PERCENT = deduction
            EMPLOYEE_RATES = employee_rates
            CERTIFICATE_RATES = certificate_rates
            LOAN_EXTRA_RATE = extra

            self.settings_result.text = (
                "✓ SETTINGS SAVED SUCCESSFULLY"
            )

        except Exception:

            self.settings_result.text = (
                "Please enter valid settings."
            )

    def back_home(self):
        self.manager.current = "home"


# ============================================================
# LATE CUSTOMERS
# ============================================================

class LateCustomerScreen(BaseScreen):

    title = "Late Customers"
    icon = "!"

    def on_enter(self):

        if self.children:
            return

        body = self.build_base()

        scroll = ScrollView(
            do_scroll_x=False
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=[dp(2), dp(2)],
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        customer = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        customer.add_widget(
            make_label(
                "Customer Name",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.late_customer = TextInput(
            hint_text="Enter customer name",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        customer.add_widget(
            self.late_customer
        )

        content.add_widget(customer)

        phone = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        phone.add_widget(
            make_label(
                "Customer Mobile Number",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.phone_input = TextInput(
            hint_text="Example: 01000000000",
            input_filter="int",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        phone.add_widget(
            self.phone_input
        )

        content.add_widget(phone)

        overdue = Card(
            bg=NAVY,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        overdue.add_widget(
            make_label(
                "Overdue Amount (EGP)",
                size=13,
                color=GOLD,
                bold=True
            )
        )

        self.overdue_input = TextInput(
            hint_text="Enter overdue amount",
            input_filter="float",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        overdue.add_widget(
            self.overdue_input
        )

        content.add_widget(overdue)

        delay = Card(
            bg=BLUE,
            orientation="vertical",
            padding=[
                dp(12),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(80)
        )

        delay.add_widget(
            make_label(
                "Delay Days",
                size=13,
                color=WHITE,
                bold=True
            )
        )

        self.delay_input = TextInput(
            hint_text="Enter number of days",
            input_filter="int",
            multiline=False,
            font_size=dp(14),
            background_color=WHITE,
            foreground_color=DARK
        )

        delay.add_widget(
            self.delay_input
        )

        content.add_widget(delay)

        generate = AppButton(
            text="GENERATE CUSTOMER MESSAGE",
            bg=GREEN2,
            size_hint_y=None,
            height=dp(48)
        )

        generate.bind(
            on_release=self.generate_message
        )

        content.add_widget(generate)

        result = Card(
            bg=DARK,
            orientation="vertical",
            padding=[
                dp(10),
                dp(8)
            ],
            size_hint_y=None,
            height=dp(210)
        )

        result.add_widget(
            make_label(
                "MESSAGE",
                size=15,
                color=GOLD,
                bold=True,
                halign="center"
            )
        )

        self.message_output = TextInput(
            text="",
            readonly=True,
            multiline=True,
            font_size=dp(12),
            background_color=(
                0.12,
                0.14,
                0.17,
                1
            ),
            foreground_color=WHITE
        )

        result.add_widget(
            self.message_output
        )

        content.add_widget(result)

        sms = AppButton(
            text="SEND SMS",
            bg=RED,
            size_hint_y=None,
            height=dp(48)
        )

        sms.bind(
            on_release=self.send_sms
        )

        content.add_widget(sms)

        back = AppButton(
            text="← BACK TO SERVICES",
            bg=BLUE2,
            size_hint_y=None,
            height=dp(45)
        )

        back.bind(
            on_release=lambda x: self.back_home()
        )

        content.add_widget(back)

        scroll.add_widget(content)

        body.add_widget(scroll)

    def generate_message(self, *args):

        name = (
            self.late_customer.text.strip()
            or "Customer"
        )

        try:
            overdue = float(
                self.overdue_input.text or 0
            )
        except Exception:
            overdue = 0

        try:
            days = int(
                self.delay_input.text or 0
            )
        except Exception:
            days = 0

        self.message_output.text = (
            "Dear "
            + name
            + ",\n\n"
            "Our records show an overdue amount of "
            + money(overdue)
            + " EGP, delayed for "
            + str(days)
            + " days.\n\n"
            "Please contact or visit the Egyptian "
            "Agricultural Bank branch to settle the "
            "outstanding amount.\n\n"
            "Thank you."
        )

    def send_sms(self, *args):

        message = (
            self.message_output.text.strip()
        )

        phone = (
            self.phone_input.text.strip()
        )

        if not message:
            self.generate_message()
            message = (
                self.message_output.text.strip()
            )

        if not phone:
            return

        try:

            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            Intent = autoclass(
                "android.content.Intent"
            )

            Uri = autoclass(
                "android.net.Uri"
            )

            intent = Intent(
                Intent.ACTION_VIEW,
                Uri.parse(
                    "sms:" + phone
                )
            )

            intent.putExtra(
                "sms_body",
                message
            )

            PythonActivity.mActivity.startActivity(
                intent
            )

        except Exception:
            pass

    def back_home(self):
        self.manager.current = "home"


# ============================================================
# APPLICATION
# ============================================================

class BankingApp(App):

    def build(self):

        self.title = (
            "Agricultural Bank Services"
        )

        Window.clearcolor = NAVY

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(
                name="home"
            )
        )

        manager.add_widget(
            AgriculturalScreen(
                name="agricultural"
            )
        )

        manager.add_widget(
            CertificateScreen(
                name="certificates"
            )
        )

        manager.add_widget(
            EmployeeLoanScreen(
                name="employee"
            )
        )

        manager.add_widget(
            SettingsScreen(
                name="settings"
            )
        )

        manager.add_widget(
            LateCustomerScreen(
                name="late"
            )
        )

        return manager


if __name__ == "__main__":
    BankingApp().run()
