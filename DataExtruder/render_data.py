from cookiecutter import generate, repository, vcs
import logging

logger = logging.getLogger()


def compile_data(template, target, data):
    context = {"cookiecutter": {"project_name": target, "data": data}}
    is_repo = repository.is_repo_url(template)
    if is_repo:
        logger.info(f"Template is a repo, cloning")
        template = vcs.clone(template, None, "remote_repos", True)
    result = generate.generate_files(
        template, context=context, overwrite_if_exists=True
    )
    return result
