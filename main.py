from flask import Flask
import utils
import view


app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.candidstes_get_all()
    html_code = view.build_html_for_some_candidates(candidates)
    return html_code


@app.route('/skills/<skill>')
def page_candidates_by_skills(skill):
    candidates = utils.candidates_get_by_skill(skill)
    html_code = view.build_html_for_some_candidates(candidates)
    return html_code


@app.route('/candidates/<int:pk>')
def page_candidate_by_pk(pk):
    candidate = utils.candidate_get_pk(pk)
    html_code = view.build_html_for_one_candidate(candidate)
    return html_code


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
#    app.run(host='127.0.0.1', port=8080, debug=False)
