import wikipedia
wikipedia.set_lang("ru")
paf = wikipedia.page("Митохондрия")
print(paf.content)