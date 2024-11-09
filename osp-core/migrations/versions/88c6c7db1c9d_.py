"""empty message

Revision ID: 88c6c7db1c9d
Revises: e87d55f476a6
Create Date: 2024-05-09 13:11:28.703925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88c6c7db1c9d'
down_revision = 'e87d55f476a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("Clips_ibfk_1", 'Clips', type_='foreignkey')
    op.create_foreign_key("clips_parentVideo_to_RecordedVideoid", 'Clips', 'RecordedVideo', ['parentVideo'], ['id'], ondelete="SET NULL")
    op.add_column('settings', sa.Column('maxClipRetention', sa.Integer(), nullable=True))
    op.add_column('Channel', sa.Column('maxClipRetention', sa.Integer(), nullable=True))
    op.add_column('Clips', sa.Column('clipDate', sa.DateTime(), nullable=True))
    op.add_column('Clips', sa.Column('owningUser', sa.Integer(), nullable=True))
    op.add_column('Clips', sa.Column('channelID', sa.Integer(), nullable=True))
    op.add_column('Clips', sa.Column('topic', sa.Integer(), nullable=True))
    op.create_foreign_key("clips_owningUser_to_userid", 'Clips', 'user', ['owningUser'], ['id'], ondelete="CASCADE")
    op.create_foreign_key("clips_channelID_to_channelid", 'Clips', 'Channel', ['channelID'], ['id'], ondelete="CASCADE")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("clips_channelID_to_channelid", 'Clips', type_='foreignkey')
    op.drop_constraint("clips_owningUser_to_userid", 'Clips', type_='foreignkey')
    op.drop_column('Clips', 'topic')
    op.drop_column('Clips', 'channelID')
    op.drop_column('Clips', 'owningUser')
    op.drop_column('Clips', 'clipDate')
    op.drop_column('Channel', 'maxClipRetention')
    op.drop_column('settings', 'maxClipRetention')
    op.drop_constraint("clips_parentVideo_to_RecordedVideoid", 'Clips', type_='foreignkey')
    op.create_foreign_key("Clips_ibfk_1", 'Clips', 'RecordedVideo', ['parentVideo'], ['id'])
    # ### end Alembic commands ###