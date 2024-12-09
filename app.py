{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de71b562-24c5-42d0-9fc7-bc29c34b2faf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "from pymongo import MongoClient\n",
    "\n",
    "# Initialize Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# MongoDB connection\n",
    "client = MongoClient(\"mongodb+srv://group6:Georgian123@group6.tzgza.mongodb.net/xyz_data?retryWrites=true&w=majority\")\n",
    "db = client['xyz_data']\n",
    "collection = db['population']\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    # Fetch data from MongoDB\n",
    "    data = list(collection.find({}, {\"_id\": 0, \"Year\": 1, \"Population\": 1}))\n",
    "\n",
    "    # Pass data to the template\n",
    "    return render_template('index.html', data=data)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, host='127.0.0.1', port=5000)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
