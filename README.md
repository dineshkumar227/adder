# PrairieProof

An automated proof grading system using a natural language web interface
  * Provides convenient interface for authoring proofs, including buttons for special characters
  * Grades set theory based proofs
  * Automatically identifies variables, sets, claims and assumptions in a proof
  * Transpiles natural language to Lean

## USAGE
  * Simply type your formatted proof into the box and hit submit to get your proof checked!
  
## INSTALLATION AND RUNNING INSTRUCTIONS
### Linux/Unix Like operating systems
   * Install lean from the [official website](https://leanprover.github.io/download/)
   * Set the `LEAN_PATH_PRAIRIE` environment variable to the path of the `lean` executable
   * Clone this repository into a folder
   * Create a python virtualenv and install the python dependencies with `pip -r requirements.txt`
   * Run the server with `python proof.py`
   * Visit the url as specified in the flask console output.

## OTHER SOURCES OF DOCUMENTATION
  * http://flask.pocoo.org/docs/1.0/
  * http://alan.blog-city.com/jquerylinedtextarea.htm
  * https://leanprover.github.io/documentation/
  
## [Contributor Guide](CONTRIBUTING.md)

## License 
Licensed under AGPL v3.0. For more details, visit [LICENSE.md](LICENSE.md)
