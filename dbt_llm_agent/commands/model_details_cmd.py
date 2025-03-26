"""
Model details command for dbt-llm-agent CLI.
"""

import click
import sys

from dbt_llm_agent.utils.logging import get_logger
from dbt_llm_agent.utils.cli_utils import (
    get_env_var,
    set_logging_level,
    colored_echo,
)

# Initialize logger
logger = get_logger(__name__)


@click.command()
@click.argument("model_name", required=True)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--json", is_flag=True, help="Output as JSON", default=False)
def model_details(model_name, verbose, json):
    """Show detailed information about a model.

    MODEL_NAME is the name of the model to get details for.
    """
    set_logging_level(verbose)

    # Import here to avoid circular imports
    from dbt_llm_agent.storage.postgres_storage import PostgresStorage

    # Load configuration from environment
    postgres_uri = get_env_var("POSTGRES_URI")

    # Validate configuration
    if not postgres_uri:
        logger.error("PostgreSQL URI not provided in environment variables (.env file)")
        sys.exit(1)

    try:
        # Initialize storage
        logger.info(f"Connecting to PostgreSQL database: {postgres_uri}")
        postgres = PostgresStorage(postgres_uri)

        # Get model
        model = postgres.get_model(model_name)
        if not model:
            logger.error(f"Model '{model_name}' not found in the database")
            sys.exit(1)

        if json:
            # Show the raw SQL code
            if model.raw_sql:
                colored_echo(f"-- SQL for model: {model_name}", color="INFO", bold=True)
                colored_echo(model.raw_sql, color="INFO")
            else:
                colored_echo(
                    f"No SQL code found for model: {model_name}", color="WARNING"
                )
        else:
            # Show readable representation
            colored_echo(model.get_readable_representation(), color="INFO")

    except Exception as e:
        logger.error(f"Error getting model details: {e}")
        sys.exit(1)
