import discord
from discord.ext import commands
from discord import app_commands
import os

# --- Configuration ---
TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# --- Le bouton qui affiche le lien ---
class PackButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # le bouton reste actif pour toujours

    @discord.ui.button(
        label="Recevoir le lien", style=discord.ButtonStyle.success, emoji="🔑"
    )
    async def get_link(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        lien = "https://canva.link/ct27lkxrz3murvw"  # <-- remplace par ton vrai lien
        await interaction.response.send_message(
            f"Voici ton accès au pack :\n{lien}",
            ephemeral=True,  # visible seulement par la personne qui clique
        )


# --- Commande slash pour poster le message avec le bouton ---
@bot.tree.command(
    name="pack", description="Affiche le message d'accès au pack avec le bouton"
)
async def pack(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔑 Accès au Pack",
        description="Clique sur le bouton ci-dessous pour recevoir ton lien d'accès en privé.",
        color=discord.Color.blurple(),
    )
    await interaction.response.send_message(embed=embed, view=PackButton())


# --- Le bouton pour le pack facture ---
class FactureButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Recevoir le lien", style=discord.ButtonStyle.success, emoji="🔑"
    )
    async def get_link(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        lien = "https://canva.link/cl8c2zs1l7uxv19"  # <-- remplace par ton vrai lien
        await interaction.response.send_message(
            f"Voici ton accès au pack facture :\n{lien}", ephemeral=True
        )


# --- Commande slash pour poster le message avec le bouton ---
@bot.tree.command(
    name="facture",
    description="Dans ce salon on te présente le pack facture, il te permettra d'accéder a de nombreuses factures modifiables.",
)
async def facture(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔑 Accès au Pack Facture",
        description="Clique sur le bouton ci-dessous pour recevoir ton lien d'accès en privé.",
        color=discord.Color.blurple(),
    )
    await interaction.response.send_message(embed=embed, view=FactureButton())


# --- Quand le bot est prêt ---
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) synchronisée(s).")
    except Exception as e:
        print(f"Erreur de synchronisation : {e}")
    print(f"Connecté en tant que {bot.user}")


bot.run(TOKEN)
