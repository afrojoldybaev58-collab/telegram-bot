import os
import sqlite3
import requests
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ================= CONFIG - EDIT TEXT HERE =================
BOT_TOKEN = os.getenv("BOT_TOKEN", "8613672548:AAFN_F8k0TI2k-V8lzcTp1v6qzKo-2-Hl5E")
CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN", "575101:AAm7fXHhh43INM4rcJJLfynVFXmvmPafCPk")
ADMIN_ID = int(os.getenv("8229546227"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://api.leadteh.ru/webhooks/crypto_pay/859590:oUEwkxLc9XN5JNbEU0TrlkoRHWGJvq4EUyIeNY2ZBc1HDojkZHJ4ww1tmYJFNxj7")

SPONSOR_PRICE = 10.0
USDT_RUB_RATE = 74.96

TEXT_START = "Welcome! Choose an option below:"
TEXT_PARSING_SUBMENU = "🧾 Receipt Parsing Menu\nChoose an option:"
TEXT_BRUTEFORCE_LOCKED = "🔍 Receipt Bruteforce\nThis is a paid service. Purchase sponsorship to access."
TEXT_BRUTEFORCE_ACCESS = "🔍 Receipt Bruteforce\nYou have access to premium features."
TEXT_FAQ = "❓ F.A.Q\n1. How does it work?\n2. What payment methods are accepted?\n3. Contact support: @support"
TEXT_REF_PROGRAM = "💰 Referral Program\nInvite friends and get 20% from their purchases.\nYour link: https://t.me/{bot_username}?start=ref_{user_id}"
TEXT_HELP = "🆘 Support\nWrite your message below and it will be sent to the admin.\nAdmin will reply to you here."
TEXT_BUY_SPONSORSHIP = f"⭐ Buy Sponsorship\nPrice: ${SPONSOR_PRICE} USD\nGet access to all premium features."
TEXT_PROFILE = """👤 User: {username}

🆔 Status: {status}
🔃 Rate: {rate} USDT/RUB

📊 Current Balance: ${balance:.2f}

📈 Checks Activated: {checks}
🪧 Total Earned: ${earned:.2f}"""
TEXT_BALANCE_PARSING = "💳 Balance Parsing\nYour balance: ${balance:.2f} USD\nPrice per check: $0.50"
TEXT_WITHDRAW = "💸 Withdrawal\nMinimum withdrawal: $5\nComing soon..."
TEXT_INVOICE_CREATED = "Invoice created for ${price} USD\nPay within 30 minutes:\n{pay_url}"
TEXT_PAYMENT_PENDING = "⏳ Waiting for payment confirmation...\nClick
