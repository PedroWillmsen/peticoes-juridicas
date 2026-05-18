import os

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "")


def get_client():
    from supabase import create_client
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)