# Spell Correction Flask app
# Copyright (C) 2021  Abigail A. Marticio

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
  
