
from django.conf.urls import url, include
from courselib.urlparts import USERID_OR_EMPLID, SLUG_RE, UNIT_SLUG, COURSE_SLUG

EVENT_TYPE = '(?P<event_type>' + SLUG_RE + ')'
EVENT_SLUG = '(?P<event_slug>' + SLUG_RE + ')'
GRANT_SLUG = '(?P<grant_slug>' + SLUG_RE + ')'
ATTACH_SLUG = '(?P<attach_slug>' + SLUG_RE + ')'

event_patterns = [ # prefix: /faculty/USERID_OR_EMPLID/events/EVENT_SLUG/
    url(r'^$', 'faculty.views.view_event', name="faculty_event_view"),
    url(r'^change$', 'faculty.views.change_event', name="faculty_change_event"),
    url(r'^change-status$', 'faculty.views.change_event_status', name="faculty_change_event_status"),
    url(r'^attach$', 'faculty.views.new_attachment'),
    url(r'^attach-text$', 'faculty.views.new_text_attachment'),
    url(r'^attach/(?P<attach_slug>' + SLUG_RE + ')/view$', 'faculty.views.view_attachment', name="faculty_view_attachment"),
    url(r'^attach/(?P<attach_slug>' + SLUG_RE + ')/download$', 'faculty.views.download_attachment', name="faculty_download_attachment"),
    url(r'^attach/(?P<attach_slug>' + SLUG_RE + ')/delete$', 'faculty.views.delete_attachment'),
    url(r'^(?P<memo_template_slug>' + SLUG_RE + ')' + '/new$', 'faculty.views.new_memo', name="faculty_event_memo_create"),
    url(r'^new-memo$', 'faculty.views.new_memo_no_template'),
    url(r'^(?P<memo_slug>' + SLUG_RE + ')' + '/manage$', 'faculty.views.manage_memo', name="faculty_event_memo_manage"),
    url(r'^_get_text/(?P<memo_template_id>' + SLUG_RE + ')' + '$', 'faculty.views.get_memo_text', name="faculty_event_memo_manage"),
    url(r'^(?P<memo_slug>' + SLUG_RE + ')' + '$', 'faculty.views.get_memo_pdf', name="faculty_event_memo_pdf"),
    url(r'^(?P<memo_slug>' + SLUG_RE + ')' + '/view$', 'faculty.views.view_memo', name="faculty_event_view_memo"),
    url(r'^(?P<memo_slug>' + SLUG_RE + ')' + '/delete$', 'faculty.views.delete_memo', name="faculty_event_delete_memo"),
    url(r'^generate_pdf/(?P<pdf_key>' + SLUG_RE + ')' + '$', 'faculty.views.generate_pdf', name="faculty_handler_generate_pdf")
]

faculty_member_patterns = [ # prefix: /faculty/USERID_OR_EMPLID/
    # Person Specific Actions
    url(r'^summary$', 'faculty.views.summary', name="faculty_summary"),
    url(r'^setup$', 'faculty.views.faculty_wizard', name="faculty_wizard"),
    url(r'^setup/(?P<position>\d+)$', 'faculty.views.faculty_wizard'),
    url(r'^otherinfo$', 'faculty.views.otherinfo', name="faculty_otherinfo"),
    url(r'^new-event$', 'faculty.views.event_type_list', name="faculty_event_types"),
    url(r'^new-event/(?P<event_type>' + SLUG_RE + ')$', 'faculty.views.create_event', name="faculty_create_event"),
    url(r'^setup/pick_position$', 'faculty.views.pick_position', name="faculty_pick_position"),

    url(r'^timeline$', 'faculty.views.timeline'),
    url(r'^timeline.json$', 'faculty.views.timeline_json'),

    url(r'^contact-info$', 'faculty.views.faculty_member_info'),
    url(r'^contact-info/edit$', 'faculty.views.edit_faculty_member_info'),

    url(r'^teaching_credit_override/' + COURSE_SLUG + '$', 'faculty.views.teaching_credit_override'),
    url(r'^salary$', 'faculty.views.salary_summary'),

    # Report:Teaching Summary
    url(r'^teaching_summary$', 'faculty.views.teaching_summary', name="faculty_teaching_summary"),
    url(r'^teaching_summary.csv$', 'faculty.views.teaching_summary_csv'),

    # Report: Study Leave Credits
    url(r'^study_leave_credits$', 'faculty.views.study_leave_credits', name="faculty_study_leave_credits"),
    url(r'^study_leave_credits.csv$', 'faculty.views.study_leave_credits_csv'),

    # Event Specific Actions
    url(r'^events/' + EVENT_SLUG + '/', include(event_patterns)),
]

faculty_patterns = [ # prefix: /faculty/
    # Top Level Stuff
    url(r'^$', 'faculty.views.index'),
    url(r'^queue$', 'faculty.views.status_index', name="status_index"),
    url(r'^members$', 'faculty.views.manage_faculty_roles'),

    # Event Searching
    url(r'^search/$', 'faculty.views.search_index'),
    url(r'^search/' + EVENT_TYPE + '$', 'faculty.views.search_events'),

    # Report: Salary
    url(r'^salaries$', 'faculty.views.salary_index'),
    url(r'^salaries.csv$', 'faculty.views.salary_index_csv'),

    # Report: Fallout
    url(r'^fallout$', 'faculty.views.fallout_report'),
    url(r'^fallout.csv$', 'faculty.views.fallout_report_csv'),

    # Report: Available Teaching Capacity
    url(r'^report/teaching_capacity$', 'faculty.views.teaching_capacity'),
    url(r'^report/teaching_capacity.csv$', 'faculty.views.teaching_capacity_csv'),

    # Report: Courses + Instructor Accreditation
    url(r'^report/course_accreditation$', 'faculty.views.course_accreditation'),
    url(r'^report/course_accreditation.csv$', 'faculty.views.course_accreditation_csv'),

    # Event Management
    url(r'^event-management$', 'faculty.views.manage_event_index', name="faculty_events_manage_index"),
    url(r'^event-management/' + EVENT_TYPE + '/$', 'faculty.views.event_config', name="template_index"),
    url(r'^event-management/' + EVENT_TYPE + '/new-memo$', 'faculty.views.new_memo_template', name="faculty_create_template"),
    url(r'^event-management/' + EVENT_TYPE + '/memos/(?P<slug>' + SLUG_RE + ')/manage$', 'faculty.views.manage_memo_template', name="faculty_manage_template"),
    url(r'^event-management/' + EVENT_TYPE + '/new-config$', 'faculty.views.event_config_add', name="faculty_create_flag"),
    #url(r'^event-management/' + EVENT_TYPE + '/memo-templates/(?P<unit>\w+)/(?P<flag>\w+)/delete-flag$', 'faculty.views.delete_event_flag', name="faculty_delete_flag"),

    # Grant Stuff
    url(r'^grants/$', 'faculty.views.grant_index', name="grants_index"),
    #url(r'^grants/new$', 'faculty.views.new_grant', name="new_grant"),
    url(r'^grants/convert/(?P<gid>\d+)$', 'faculty.views.convert_grant', name="convert_grant"),
    url(r'^grants/delete/(?P<gid>\d+)$', 'faculty.views.delete_grant', name="delete_grant"),
    url(r'^grants/import$', 'faculty.views.import_grants', name="import_grants"),
    url(r'^grants/' + UNIT_SLUG + '/' + GRANT_SLUG + '$', 'faculty.views.view_grant', name="view_grant"),
    url(r'^grants/' + UNIT_SLUG + '/' + GRANT_SLUG + '/edit$', 'faculty.views.edit_grant', name="edit_grant"),

    # faculty-member hierarchy
    url(r'^' + USERID_OR_EMPLID + '/', include(faculty_member_patterns)),

    # Positions
    url(r'^positions/$', 'faculty.views.list_positions'),
    url(r'^positions/new_position$', 'faculty.views.new_position'),
    url(r'^positions/(?P<position_id>\d+)/edit_position/$', 'faculty.views.edit_position'),
    url(r'^positions/(?P<position_id>\d+)/delete_position/$', 'faculty.views.delete_position'),
    url(r'^positions/(?P<position_id>\d+)/view_position/$', 'faculty.views.view_position'),
    url(r'^positions/(?P<position_id>\d+)/assign_position_entry/$', 'faculty.views.assign_position_entry'),
    url(r'^positions/(?P<position_id>\d+)/assign_position_person/$', 'faculty.views.assign_position_person'),
    url(r'^positions/(?P<position_id>\d+)/assign_position_futureperson/$', 'faculty.views.assign_position_futureperson'),
    url(r'^positions/(?P<position_id>\d+)/add_position_credentials/$', 'faculty.views.position_add_credentials'),
    url(r'^positions/(?P<position_id>\d+)/yellow1/$', 'faculty.views.position_get_yellow_form_tenure'),
    url(r'^positions/(?P<position_id>\d+)/yellow2/$', 'faculty.views.position_get_yellow_form_limited'),
    url(r'^positions/(?P<position_id>\d+)/new_attach', 'faculty.views.new_position_attachment'),
    url(r'^positions/(?P<position_id>\d+)/' + ATTACH_SLUG + '/delete$', 'faculty.views.delete_position_attachment'),
    url(r'^positions/(?P<position_id>\d+)/' + ATTACH_SLUG + '/view', 'faculty.views.view_position_attachment'),
    url(r'^positions/(?P<position_id>\d+)/' + ATTACH_SLUG + '/download$', 'faculty.views.download_position_attachment'),


    # Future Person Management
    url(r'^(?P<futureperson_id>\d+)/edit_futureperson/$', 'faculty.views.edit_futureperson'),
    url(r'^(?P<futureperson_id>\d+)/edit_futureperson/(?P<from_admin>\d)/$', 'faculty.views.edit_futureperson'),
    url(r'^(?P<futureperson_id>\d+)/view_futureperson/$', 'faculty.views.view_futureperson'),
    url(r'^(?P<futureperson_id>\d+)/view_futureperson/(?P<from_admin>\d)/$', 'faculty.views.view_futureperson'),
    url(r'^(?P<futureperson_id>\d+)/delete_futureperson/$', 'faculty.views.delete_futureperson')
]
