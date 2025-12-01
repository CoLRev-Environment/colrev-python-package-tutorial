import colrev.package_manager.package_base_classes as base_classes
import colrev.record.record

class JournalAbbreviationPrep(base_classes.PrepPackageBaseClass):

    def __init__(self, prep_operation, settings):
        super().__init__(prep_operation, settings)

    def prepare(self, record: colrev.record.record.Record) -> colrev.record.record.Record:
        """Standardizes journal names in a CoLRev record"""

        if 'journal' in record.data:
            journal = record.data['journal']

            standardized_journal = self.standardize_journal_name(journal)
            record.update_field(
                key='journal', 
                value=standardized_journal, 
                source='journal_abbreviation_prep'
            )
        return record

    def standardize_journal_name(self, name: str) -> str:
        """Our original function lives here."""
        abbreviations = {
            "Int": "International",
            "J": "Journal",
            "Comput": "Computing",
            "Syst": "Systems",
            "Sci": "Science",
        }
        words = name.split()
        standardized_words = [abbreviations.get(word, word) for word in words]
        return " ".join(standardized_words)