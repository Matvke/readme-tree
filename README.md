# readme-tree

Create a directory tree and save it in a readme file.

# Example of generated directory tree
```
api_creater/
│   ├── .env
│   ├── .gitignore
│   ├── alembic.ini
│   ├── LICENSE
│   ├── README.md
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │   │   ├── routes.py
│   │   │   │   └── endpoints/
│   │   │   │       ├── auth.py
│   │   │   │       └── user.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── dependencies.py
│   │   │   ├── enums.py
│   │   │   └── security.py
│   │   ├── dependencies/
│   │   │   ├── auth_dependencies.py
│   │   │   ├── repository_dependencies.py
│   │   │   └── service_dependencies.py
│   │   ├── exceptions/
│   │   │   ├── exception_handlers.py
│   │   │   ├── http_exceptions.py
│   │   │   └── service_exceptions.py
│   │   ├── model/
│   │   │   └── models.py
│   │   ├── repository/
│   │   │   ├── base_repository.py
│   │   │   ├── post_repository.py
│   │   │   └── user_repository.py
│   │   ├── schemas/
│   │   │   ├── auth_request.py
│   │   │   ├── auth_response.py
│   │   │   └── security_schema.py
│   │   └── services/
│   │       ├── auth_service.py
│   │       └── user_service.py
│   ├── migration/
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/
│   │       ├── 095ec926e9eb_rename_column_users_name_to_users_.py
│   │       ├── 0bf6f180d102_is_active_base_column_now.py
│   │       ├── a6e07ec20d38_rename_password_to_hashed_password.py
│   │       ├── bd91fdb42bba_added_column_disabled_for_soft_delete.py
│   │       ├── c0491b7be7cb_initial_revision.py
│   │       ├── cc364f1a07f4_removed_cloumn_is_added_from_base_model_.py
│   │       └── f49d64b7d43d_username_unique_now.py
│   └── tests/
```