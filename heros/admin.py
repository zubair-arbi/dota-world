from django.contrib import admin

from heros.models import Hero, HeroRole, HeroAdvantage


class HeroTypeInline(admin.StackedInline):
    model = HeroRole
    extra = 1


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'attack_type')
    search_fields = ['name', 'category', 'attack_type']
    ordering = ('-category', '-name', '-attack_type')
    inlines = [HeroTypeInline]


class HeroRoleAdmin(admin.ModelAdmin):
    list_display = ('hero', 'role', 'level', 'win_rate')
    search_fields = ['hero', 'role', 'level']
    ordering = ('-hero', '-role', '-level', 'win_rate')


class HeroAdvantageAdmin(admin.ModelAdmin):
    list_display = ('hero', 'opponent_hero', 'advantage', 'win_rate', 'matches_played')
    search_fields = ['hero', 'opponent_hero']
    ordering = ('hero', '-advantage', 'win_rate', '-matches_played',)

admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroRole, HeroRoleAdmin)
admin.site.register(HeroAdvantage, HeroAdvantageAdmin)
