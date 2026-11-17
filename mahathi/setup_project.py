import os

structure = {
    "backend": {
        "app": {
            "models": ["__init__.py", "user.py", "menu.py", "order.py", "table.py", "customer.py", "payment.py"],
            "routes": ["__init__.py", "auth.py", "menu.py", "orders.py", "tables.py", "customers.py", "payments.py"],
            "schemas": ["user_schema.py", "menu_schema.py", "order_schema.py"],
            "services": ["auth_service.py", "order_service.py"],
            "utils": ["security.py"],
            "files": ["__init__.py", "main.py", "database.py"]
        },
        "files": ["migrations/", "tests/", "venv/", ".env", ".gitignore", "requirements.txt", "run.py"]
    },
    "frontend": {
        "public": [],
        "src": {
            "components": {
                "common": [],
                "layout": [],
                "dashboard": []
            },
            "pages": ["Login.jsx", "Dashboard.jsx", "Menu.jsx", "Orders.jsx", "POS.jsx", "Tables.jsx", "Reservations.jsx", "Customers.jsx", "Reports.jsx"],
            "services": ["api.js", "authService.js", "menuService.js", "orderService.js"],
            "styles": [],
            "files": ["assets/", "context/", "hooks/", "App.jsx", "main.jsx"]
        },
        "files": [".env", "package.json", "vite.config.js", "index.html"]
    },
    "root_files": ["README.md", ".gitignore"]
}

def create_structure(base_path, struct):
    for key, value in struct.items():
        if key == "files":
            for file in value:
                if file.endswith("/"):
                    os.makedirs(os.path.join(base_path, file), exist_ok=True)
                else:
                    file_path = os.path.join(base_path, file)
                    if not os.path.exists(file_path):
                        with open(file_path, "w") as f:
                            f.write("")
        elif key == "root_files":
            for file in value:
                file_path = os.path.join(base_path, file)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        f.write("")
        elif isinstance(value, dict):
            dir_path = os.path.join(base_path, key)
            os.makedirs(dir_path, exist_ok=True)
            create_structure(dir_path, value)

if __name__ == "__main__":
    print("🚀 Generating Mahathi Project Structure...")
    create_structure(".", structure)
    print("✅ Project structure successfully generated!")