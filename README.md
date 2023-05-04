
# Science Graph Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A plugin for AutoGPT to access to all scholarly articles, publications, preprints, or works with a DOI, ORCID, ROR or other scholarly identifiers
## Installation

To install in AutoGPT, copy the zipped repository into the `/plugins` folder in AutoGPT and add the name of the plugin in the .env file: 


```bash
ALLOWLISTED_PLUGINS=AutoGPTPluginScienceGraph
```

You will also need to run the [Run the dependency install script for plugins](https://github.com/Significant-Gravitas/Auto-GPT-Plugins#installation)

```bash
python -m autogpt --install-plugin-deps
```


## Usage

AutoGPT will use the command 'search_scholarly_works' to find scholarly articles, publications, preprints, or works with a DOI, ORCID, ROR or other scholarly identifiers.

```bash
17. message_agent: Message GPT Agent, args: "key": "<key>", "message": "<message>"
18. start_agent: Start GPT Agent, args: "name": "<name>", "task": "<short_task_desc>", "prompt": "<prompt>"
19. Task Complete (Shutdown): "task_complete", args: "reason": "<reason>"
20. search_scholarly_works: "Search any scholarly article", args: "keyword": "<keyword>"
21. search_journal_articles: "Search journal articles", args: "keyword": "<keyword>"
```
## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgements

- AutoGPT project
- DataCite
- Crossref
