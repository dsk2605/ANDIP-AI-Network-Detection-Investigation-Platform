from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool, text

from alembic import context

# Alembic Config object
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import metadata
from app.database.base import Base
from app.models.asset import Asset

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # ==========================
    # DEBUG INFORMATION
    # ==========================
    with connectable.connect() as conn:
        print("\n" + "=" * 70)
        print("ALEMBIC DATABASE DEBUG")
        print("=" * 70)

        print(
            "Database:",
            conn.execute(text("SELECT current_database()")).scalar(),
        )

        print(
            "Schema:",
            conn.execute(text("SELECT current_schema()")).scalar(),
        )

        print(
            "Current User:",
            conn.execute(text("SELECT current_user")).scalar(),
        )

        print(
            "Server Address / Port:",
            conn.execute(
                text("SELECT inet_server_addr(), inet_server_port()")
            ).fetchone(),
        )

        print(
            "Server Port (SHOW):",
            conn.execute(text("SHOW port")).scalar(),
        )

        print(
            "Existing Tables:",
            conn.execute(
                text(
                    """
                    SELECT tablename
                    FROM pg_tables
                    WHERE schemaname='public'
                    """
                )
            ).fetchall(),
        )

        print(
            "Existing Enums:",
            conn.execute(
                text(
                    """
                    SELECT typname
                    FROM pg_type
                    WHERE typname IN (
                        'assettype',
                        'environmenttype',
                        'assetstatus'
                    )
                    """
                )
            ).fetchall(),
        )

        print("=" * 70 + "\n")

    # ==========================
    # RUN MIGRATIONS
    # ==========================
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()