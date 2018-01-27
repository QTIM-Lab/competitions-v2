from drf_extra_fields.fields import Base64ImageField
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from api.serializers.leaderboards import LeaderboardSerializer
from competitions.models import Competition, Phase, Submission, Page
from profiles.models import User


class PhaseSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Phase
        fields = (
            'id',
            'number',
            'start',
            'end',
            'description',
            'input_data',
            'reference_data',
            'scoring_program',
            'ingestion_program',
            'public_data',
            'starting_kit',
        )


class PageSerializer(WritableNestedModelSerializer):
    # *NOTE* The competition property has to be replicated at the end of the file
    # after the CompetitionSerializer class is declared
    # competition = CompetitionSerializer(many=True)

    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'content',
            'index',
        )


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('phase',)


class CompetitionSerializer(WritableNestedModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    logo = Base64ImageField(required=True)
    pages = PageSerializer(many=True)
    phases = PhaseSerializer(many=True)
    leaderboards = LeaderboardSerializer(many=True)
    collaborators = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Competition
        fields = (
            'id',
            'title',
            'created_by',
            'logo',
            'pages',
            'phases',
            'leaderboards',
            'collaborators',
        )

    def get_created_by(self, object):
        return str(object.created_by)

    def validate_leaderboards(self, value):
        if not value:
            raise serializers.ValidationError("Competitions require at least 1 leaderboard")
        return value


PageSerializer.competition = CompetitionSerializer(many=True, source='competition')
