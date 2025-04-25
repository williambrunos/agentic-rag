from app.services.agent import alfred
import asyncio
from datetime import datetime
import pandas as pd


INPUT_QUESTIONS_CSV_DIR = "tests/questions/questions.csv"
OUTPUT_QUESTIONS_CSV_DIR = f"tests/question_results/results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"


async def test_alfred():
    df_questions = pd.read_csv(INPUT_QUESTIONS_CSV_DIR)
    if 'question' not in df_questions.columns:
        raise ValueError("O CSV de entrada precisa ter uma coluna 'question'")

    records = []
    for idx, row in df_questions.iterrows():
        q = row['question']
        try:
            resp = await alfred.run(q)
            answer = resp.response if hasattr(resp, 'response') else str(resp)
        except Exception as e:
            answer = f"ERROR: {e}"
        records.append({
            'question': q,
            'response': answer,
            'execution_date': datetime.now().isoformat()
        })
        print(f"✅ Pergunta: {q!r}  → Resposta: {answer!r}")

    df_results = pd.DataFrame(records)

    df_results.to_csv(OUTPUT_QUESTIONS_CSV_DIR, index=False, encoding='utf-8-', sep=";")
    print(f"\nResultados salvos em: {OUTPUT_QUESTIONS_CSV_DIR}")

    return df_results



if __name__ == "__main__":
    asyncio.run(test_alfred())
