from flask import Flask, render_template
from flask import Blueprint
from repositories import product_repository

product_repository = Blueprint("products", __name__)