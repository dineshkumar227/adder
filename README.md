# Adder

Input a proof in plain English in the web interface, and recieve immediate feedback on whether it is right or not, and how to fix it!
  * Provides convenient interface for authoring proofs, including buttons for special characters
  * Recieve feedback on where in the proof you're wrong if there are any mistakes
  * Useful for: 
    - Checking whether your homework is correct
    - Automatically grade tests/exams without human intervention
    - Writing informal proofs while still checking for correctness
  
  
# Technical Details
  * Grades set theory based proofs
  * Automatically identifies variables, sets, claims and assumptions in a proof
  * Transpiles using NLP techniques to Lean, a programming language meant for proof checking 

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
Licensed under AGPL v3.0. For more details, visit [LICENSE](LICENSE)
