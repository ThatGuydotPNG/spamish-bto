import discord
from discord.ext import commands
from Model import detect_bird

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos logeado como: {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola! Soy {bot.user}!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! I am {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)


@bot.command()
async def subir_imagen(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No se ha encontrado ninguna imagen adjunta.")
    else:
        # Iterar sobre los archivos adjuntos
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(('jpg', 'jpeg', 'png', 'gif')):
                # Guardar la imagen en el sistema de archivos local
                filepath = f"{attachment.filename}"
                await attachment.save(filepath)
                
                # Enviar la URL de la imagen de vuelta al usuario
                await ctx.send(f"Imagen {attachment.filename} guardada con éxito. Disponible en: {attachment.url}")

                result = detect_bird(filepath)
                await ctx.send(result)


            else:
                await ctx.send(f"El archivo {attachment.filename} no es una imagen válida.")

@bot.command()
async def upload_image(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No image found in the attachments.")
    else:
        # Iterate over the attachments
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(('jpg', 'jpeg', 'png', 'gif')):
                # Save the image to the local file system
                filepath = f"{attachment.filename}"
                await attachment.save(filepath)

                # Send the URL of the image back to the user
                await ctx.send(f"Image {attachment.filename} saved successfully. Available at: {attachment.url}")


            else:
                await ctx.send(f"The archive {attachment.filename} is not a valid image.")                

@bot.command()
async def thefog(ctx):
    await ctx.send("the fog is coming... the fog will rip your intestines out and make you eat them😂 then, it will consume the sky, the sun, the moon, because? we forgot to feed it, we forgot the 28 corpses in the basement!!😂😂😂😂🤣🤣")

@bot.command()
async def laniebla(ctx):
    await ctx.send("la niebla viene... la niebla te arrancará los intestinos y te hará comértelos😂 luego, consumirá el cielo, el sol, la luna, ¿por qué? ¡porque olvidamos alimentarla, olvidamos los 28 cadáveres en el sótano!😂😂😂😂🤣🤣")    

@bot.command()
async def welcome(ctx):
    await ctx.send("Welcome to the server! If you have any questions, feel free to ask using $englishcommands. Enjoy your stay! 😊")
    
@bot.command()
async def bienvenido(ctx):
    await ctx.send("¡Bienvenido al servidor! Si tienes alguna pregunta, no dudes en preguntar usando $comandosespañoles. ¡Disfruta tu estadía! 😊")

@bot.command()
async def silly(ctx):
    await ctx.send("Silly goose! 🦢")

@bot.command()
async def chistoso(ctx):
    await ctx.send("Ganso chistoso! 🦢")

@bot.command()
async def englishcommands(ctx):
    await ctx.send("Here are some commands you can use:\n"
                 "$heh [count] - Repeat 'heh' a specified number of times (default is 5)\n"
                 "$upload_image - Upload an image to the server\n"
                 "$thefog - don't talk about it.'\n"
                 "$welcome - Get a welcome message\n"
                "$hello - Say hello to the bot\n")

@bot.command()
async def comandosespañoles(ctx):
    await ctx.send("Aquí hay algunos comandos que puedes usar:\n"
                 "$heh [count] - Repetir 'heh' un número especificado de veces (el valor predeterminado es 5)\n"
                 "$subir_imagen - Subir una imagen al servidor\n"
                 "$laniebla - no hables de eso.\n"
                 "$bienvenido - Obtener un mensaje de bienvenida\n"
                 "$hola - Saludar al bot\n")

bot.run("MTM4MjgzMDYxNTk4ODI3MzIwMg.GnSfSH.TFBjPojSn4G_MbAkHLaXTkn9TtrRl7FHgPmpAI")