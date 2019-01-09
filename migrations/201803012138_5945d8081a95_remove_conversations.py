"""Remove conversations

Revision ID: 5945d8081a95
Revises: af3f5579c84d
Create Date: 2018-03-01 21:38:34

"""
from alembic import op
import sqlalchemy as sa
import flaskbb
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '5945d8081a95'
down_revision = '232e68a03aa2'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Not sure if deleting them is a good idea.. all data would be lost
    #op.drop_table('messages')
    #op.drop_table('conversations')
    # ### end Alembic commands ###
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.create_table('conversations',
    #sa.Column('id', sa.Integer(), nullable=False),
    #sa.Column('user_id', sa.Integer(), nullable=False),
    #sa.Column('from_user_id', sa.Integer(), nullable=True),
    #sa.Column('to_user_id', sa.Integer(), nullable=True),
    #sa.Column('shared_id', sqlalchemy_utils.types.uuid.UUIDType(binary=16), nullable=False),
    #sa.Column('subject', sa.String(length=255), nullable=True),
    #sa.Column('date_created', flaskbb.utils.database.UTCDateTime(timezone=True), nullable=False),
    #sa.Column('date_modified', flaskbb.utils.database.UTCDateTime(timezone=True), nullable=False),
    #sa.Column('trash', sa.Boolean(), nullable=False),
    #sa.Column('draft', sa.Boolean(), nullable=False),
    #sa.Column('unread', sa.Boolean(), nullable=False),
    #sa.ForeignKeyConstraint(['from_user_id'], ['users.id'], name=op.f('fk_conversations_from_user_id_users'), ondelete='SET NULL'),
    #sa.ForeignKeyConstraint(['to_user_id'], ['users.id'], name=op.f('fk_conversations_to_user_id_users'), ondelete='SET NULL'),
    #sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_conversations_user_id_users'), ondelete='CASCADE'),
    #sa.PrimaryKeyConstraint('id', name=op.f('pk_conversations'))
    #)
    #op.create_table('messages',
    #sa.Column('id', sa.Integer(), nullable=False),
    #sa.Column('conversation_id', sa.Integer(), nullable=False),
    #sa.Column('user_id', sa.Integer(), nullable=True),
    #sa.Column('message', sa.Text(), nullable=False),
    #sa.Column('date_created', flaskbb.utils.database.UTCDateTime(timezone=True), nullable=False),
    #sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], name=op.f('fk_messages_conversation_id_conversations'), ondelete='CASCADE'),
    #sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_messages_user_id_users'), ondelete='SET NULL'),
    #sa.PrimaryKeyConstraint('id', name=op.f('pk_messages'))
    #)
    # ### end Alembic commands ###
    pass
