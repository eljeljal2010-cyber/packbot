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
        title="Accès au Pack materiel",
        description="Dans se salon on te présente le pack materiel, il sert a quoi ? Il te permettera de te lancer dans les meilleur conditions grâce au materiels indispensable qu'on te montre dedans.",
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
    description="Affiche le message d'accès au pack facture",
)
async def facture(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Accès au Pack Facture",
        description="Dans ce salon on te présente un pack contenant plus de 100 factures cents pour cents modifiable.",
        color=discord.Color.blurple(),
    )
    await interaction.response.send_message(embed=embed, view=FactureButton())

# --- Le bouton pour le pack fournisseurs ---
class FournisseursButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Recevoir le lien", style=discord.ButtonStyle.success, emoji="🔑")
    async def get_link(self, interaction: discord.Interaction, button: discord.ui.Button):
        lien = "https://canva.link/xx1e6g303g9mr66"
        await interaction.response.send_message(
            f"Voici ton accès au pack fournisseurs :\n{lien}",
            ephemeral=True
        )


# --- Commande slash pour poster le message avec le bouton ---
@bot.tree.command(name="fournisseurs", description="Affiche le message d'accès au pack fournisseurs")
async def fournisseurs(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Accès au Pack Fournisseurs",
        description="Dans ce salon tu retrouveras un pack essentiel à l'achat revente, dedans tu retrouveras 7 fournisseurs dont 2 authentique, si tu veux te lancer ce pack est fait pour toi.",
        color=discord.Color.blurple()
    )
    await interaction.response.send_message(embed=embed, view=FournisseursButton())

# --- Le bouton pour le pack niche ---
class Niche2Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Recevoir le lien", style=discord.ButtonStyle.success, emoji="🔑")
    async def get_link(self, interaction: discord.Interaction, button: discord.ui.Button):
        lien = "https://canva.link/0e3zd56ngc9jasz"
        await interaction.response.send_message(
            f"Voici ton accès au pack niche 2 :\n{lien}",
            ephemeral=True
        )


# --- Commande slash pour poster le message avec le bouton ---
@bot.tree.command(name="niche2", description="Affiche le message d'accès au pack niche 2")
async def niche(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Accès au Pack Niche 2ème version",
        description="Dans ce salon tu retrouveras deux version du pack niches, on te présente la 2ème version du pack niche, ou tu retrouveras des niches 100% rentable (attention: avec le temps les niches du pack peuvent se vendre moins chère ou moins rapidement).",
        color=discord.Color.blurple()
    )
    await interaction.response.send_message(embed=embed, view=NicheButton())

# --- Le bouton pour le pack niche ---
class NicheButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Recevoir le lien", style=discord.ButtonStyle.success, emoji="🔑")
    async def get_link(self, interaction: discord.Interaction, button: discord.ui.Button):
        lien = "https://canva.link/s8f14ty0y7nbuq5"
        await interaction.response.send_message(
            f"Voici ton accès au pack niche 2 :\n{lien}",
            ephemeral=True
        )


# --- Commande slash pour poster le message avec le bouton ---
@bot.tree.command(name="niche", description="Affiche le message d'accès au pack niche")
async def niche(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔑 Accès au Pack Niche",
        description="Clique sur le bouton ci-dessous pour recevoir ton lien d'accès en privé.",
        color=discord.Color.blurple()
    )
    await interaction.response.send_message(embed=embed, view=NicheButton())


# --- Quand le bot est prêt ---
GUILD_ID = discord.Object(id=1521237058591395890)

@bot.event
async def on_ready():
    try:
        bot.tree.copy_global_to(guild=GUILD_ID)
        synced = await bot.tree.sync(guild=GUILD_ID)
        print(f"{len(synced)} commande(s) synchronisée(s) sur le serveur.")
    except Exception as e:
        print(f"Erreur de synchronisation : {e}")
    print(f"Connecté en tant que {bot.user}")


bot.run(TOKEN)
