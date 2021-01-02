from flask import Flask, request
from spell_correction import SpellCorrection


app = Flask(__name__)


@app.route("/spell-correction", methods=["GET"])
def get_correction():
  spell_correction = SpellCorrection(data="assets/spell-errors.txt")
  text = request.args.get("word", default=None)
  correct_text = spell_correction.get_correction(text)
  return f"{text} => {correct_text}"
  
  
  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
  
