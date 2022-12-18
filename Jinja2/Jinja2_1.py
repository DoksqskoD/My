import jinja2

name = "Koli"

tm = jinja2.Template("Hello {{name}}")

msg = tm.render(name = name)

print(msg)

### Конструкция {{}}
### {%%} - Спецификатор шаблона
### {{}} - Выражение для вставки конструкции Python в шаблон
###