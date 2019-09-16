# services/users/manage.py

from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)

# The command name is changed and as actually recreate-db not with the underscore
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()