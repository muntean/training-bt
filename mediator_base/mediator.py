import logging

_logger = logging.getLogger(__name__)

class MediatorError(Exception): pass

class MediatorBase:
    """
    Base Mediator class — defines generic logic for executing remote or local operations.
    """

    # class_name → route/method mapping
    mapping = {
        # 'DTOFetchExistingContact': {
        #     'target': '/user_profile/get_existing_contact_address',
        #     'method': 'fetch_existing_contact',
        #     'result': 'DTOFetchExistingContactResult'
        # }
    }

    def __init__(self, runner_obj=None, forcenull=False, gateway=False):
        """
        :param runner_obj: instance of MediatorRunner
        """
        if not runner_obj and not forcenull:
            raise MediatorError("Null runner! Not supported.")
        self.runner = runner_obj
        self.gateway = gateway

    # ----------------------------- #
    # Helpers
    # ----------------------------- #

    def get_mapping(self):
        """Return the mapping dictionary."""
        return self.mapping

    def _get_target_details(self, dto):
        """Retrieve mapping info for a given DTO class name."""
        class_name = dto.__class__.__name__
        return self.mapping.get(class_name, {})

    # ----------------------------- #
    # Main Call Logic
    # ----------------------------- #

    def call(self, dto):
        """
        Execute operation associated with the DTO.

        - If mapping defines 'method', invokes that method on self.
        - If 'target' exists and runner is defined, delegates to runner.
        - Otherwise, raises clear exceptions.
        """
        if dto is None:
            raise ValueError("Not supported: Null DTO")

        target_details = self._get_target_details(dto)
        if not target_details:
            raise NotImplementedError(
                f"No mapping defined for DTO class '{dto.__class__.__name__}'"
            )

        target_name = target_details.get("target")
        method_name = target_details.get("method")
        result = None

        # Prefer calling runner if defined
        if target_name and self.runner:
            try:
                result = self.runner.call(target_name, dto.to_json())
            except Exception as e:
                _logger.exception(f"Error while calling runner for target '{target_name}': {e}")
                raise

        # Otherwise, fallback to internal mediator method
        elif method_name:
            try:
                method = getattr(self, method_name)
                result = method(dto)
            except AttributeError:
                _logger.error(f"Method '{method_name}' not found in mediator '{self.__class__.__name__}'")
                raise
            except Exception as e:
                _logger.exception(f"Error executing mediator method '{method_name}': {e}")
                raise

        else:
            raise NotImplementedError(
                f"Mapping for '{dto.__class__.__name__}' must define at least one of ['method', 'target']"
            )

        return result