class Spell:
    def __init__(self, name, school, level, cast_limit, effect):
        self.name = name
        self.school = school
        if type(level != int) and (level < 0 or level > 9):
            raise ValueError("Invalid spell level specified.")
        self.level = level
        self.cast_limit = cast_limit
        self.effect = effect
        self.casts = cast_limit

    def cast(self):
        if self.casts <= 0:
            print("Can't cast {} any more today.".format(self.name))
        else:
            self.casts -= 1
            print("Casting {}...".format(self.name))
            print(self.effect)
            print("You can cast {} {} more time(s) today.".format(self.name, self.casts))
            print("")

    def recharge(self):
        self.casts = self.cast_limit
    
    def get_name(self):
        return self.name
    def get_school(self):
        return self.school
    def get_level(self):
        return self.level
    def get_cast_limit(self):
        return self.cast_limit
    def get_effect(self):
        return self.effect

class Spellbook:
    def __init__(self, material, capacity):
        self.material = material
        self.capacity = int(capacity)
        self.spells = []
        self.total = 0

    def add_spell(self, new_spell):
        if (self.total + new_spell.level) > self.capacity:
            raise ValueError("We're nearing the end of our power budget. You can't write {} into this spellbook.").format(new_spell.name)
        self.spells.append(new_spell)
        self.total += new_spell.level

    def cast_spell(self, s):
        i = 0
        while i < len(self.spells):
            if self.spells[i].name == s:
                self.spells[i].cast()
                return
            else:
                print("There is no spell called {} here.").format(name)

    #def cast_strongest(self):
    #    j = 0
    #    while j < len(self.spells):

    
tablet = Spellbook('Stone', 24)
post_it_note = Spellbook('Paper', 3)
tickle = Spell('Tickle', 'Evocation', 0, 100, "You point at a target and watch them squirm as an invisible feather begins tickling at their sides! Or not. Some people aren't ticklish.") 
castle = Spell("Queen Elsa's Instant Castle", 'Transmutation', 8, 1, "You sing a showstopping Broadway tune and build an ice castle out of basically nothing. That feels pretty great.")
cheesecake = Spell("Cheesecake Calamity", 'Conjuration', 8, 5, "You mutter a few words and a slice of cheesecake spontaneously appears on a point that you can see within range. Then two slices. Then four. Then eight. Sixteen. Thirty-two. Oh no...") 
anti_cheesecake = Spell("Destroy Cheesecake", 'Evocation', 7, 3, "For the next five minutes, any continuous segment of cheesecake you touch immediately disintegrates. It tastes lovely.") 
f_ball = Spell("Fireball", 'Evocation', 3, 3, "You crush a bit of charcoal between your fingers and specify a point within 120 feet. An explosion of heat and light (and smoke!) expands from that point, and it's just SO PRETTY.")

post_it_note.add_spell(tickle)
post_it_note.add_spell(f_ball)
try:
    post_it_note.add_spell(cheesecake)
except ValueError as e:
    print(e)
post_it_note.cast_spell("Destroy Cheesecake") 
post_it_note.cast_spell("Fireball") 

