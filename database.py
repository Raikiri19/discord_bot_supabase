import os
from supabase import create_client, Client

# Vom lua aceste valori din variabilele de sistem (Environment Variables)
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def add_points(discord_id: str, points_to_add: int):
    # 1. Verificăm dacă userul există
    response = supabase.table("users").select("*").eq("user_id", discord_id).execute()

    if not response.data:
        # Dacă nu există, îl creăm
        data = {"user_id": discord_id, "points": points_to_add}
        supabase.table("users").insert(data).execute()
        return points_to_add
    else:
        # Dacă există, îi actualizăm punctele
        current_points = response.data[0]['points']
        new_total = current_points + points_to_add
        supabase.table("users").update({"points": new_total}).eq("user_id", discord_id).execute()
        return new_total

def get_points(discord_id: str):
    response = supabase.table("users").select("points").eq("user_id", discord_id).execute()
    if response.data:
        return response.data[0]['points']
    return 0