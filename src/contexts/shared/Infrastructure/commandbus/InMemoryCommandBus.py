from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.CommandHandler import CommandHandler
from src.contexts.shared.domain.errors.CommandNoRegisteredError import CommandNotRegisteredError


class InMemoryCommandBus(BaseObject, CommandBus):

    def __init__(self, *handlers: CommandHandler):
        handler_mapping = {}
        for handler in handlers:
            handler_mapping[handler.subscribed_to()] = handler
        self._handler_mapping: dict[str, CommandHandler] = handler_mapping

    def _search(self, command_name: str) -> CommandHandler | None:
        if command_name not in self._handler_mapping:
            raise CommandNotRegisteredError()
        return self._handler_mapping[command_name]

    async def dispatch(self, command: Command):
        query_type: str = command.get_command_type_name()
        handler = self._search(query_type)
        return await handler.handle(command)
