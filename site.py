from staticpipes.config import Config
from staticpipes.pipes.copy import PipeCopy
from staticpipes.pipes.jinja2 import PipeJinja2
from staticpipes.pipes.exclude_underscore_directories import PipeExcludeUnderscoreDirectories
from staticpipes.pipes.exclude_dot_directories import PipeExcludeDotDirectories
from staticpipesdatatig.pipes.load_datatig import PipeLoadDatatig
from staticpipes.pipes.collection_records_process import PipeCollectionRecordsProcess
from staticpipes.processes.jinja2 import ProcessJinja2

import os

config = Config(
    pipes=[
        PipeExcludeDotDirectories(),
        PipeExcludeUnderscoreDirectories(),
        PipeCopy(extensions=["css", "txt"]),
        PipeLoadDatatig(),
        PipeJinja2(),
        PipeCollectionRecordsProcess(
            collection_name="event",
            processors=[
                ProcessJinja2(template="_templates/event.html")
            ],
            output_dir="event",
            context_key_record_id="event_id",
            context_key_record_data="event"
        ),
        PipeCollectionRecordsProcess(
            collection_name="blog",
            processors=[
                ProcessJinja2(template="_templates/blog.html")
            ],
            output_dir="blog",
            context_key_record_id="blog_id",
            context_key_record_data="blog"
        ),
    ],
)

if __name__ == "__main__":
    from staticpipes.cli import cli
    cli(
        config,
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"),
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "_site")
    )
