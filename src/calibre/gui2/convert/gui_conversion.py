# -*- coding: utf-8 -*-

__license__ = 'GPL 3'
__copyright__ = '2009, John Schember <john@nachtimwald.com>'
__docformat__ = 'restructuredtext en'

from calibre.ebooks.conversion.plumber import Plumber
from calibre.utils.logging import Log
from calibre.customize.conversion import OptionRecommendation, DummyReporter

def gui_convert(input, output, recommendations, notification=DummyReporter(),
        abort_after_input_dump=False, log=None):
    recommendations = list(recommendations)
    recommendations.append(('verbose', 2, OptionRecommendation.HIGH))
    if log is None:
        log = Log()
    plumber = Plumber(input, output, log, report_progress=notification,
            abort_after_input_dump=abort_after_input_dump)
    plumber.merge_ui_recommendations(recommendations)

    plumber.run()

def gui_catalog(fmt, title, dbspec, ids, out_file_name,
        notification=DummyReporter(), log=None):
    if log is None:
        log = Log()
    if dbspec is None:
        from calibre.utils.config import prefs
        from calibre.library.database2 import LibraryDatabase2
        dbpath = prefs['library_path']
        db = LibraryDatabase2(dbpath)
    else: # To be implemented in the future
        pass
    # Implement the interface to the catalog generating code here
    db




