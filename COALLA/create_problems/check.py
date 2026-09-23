"""PyCharm에서 이 파일을 실행하세요. 아래 경로 두 개를 수정하면 됩니다."""
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import psutil

# 상대 경로는 이 스크립트가 있는 폴더를 기준으로 합니다.
BASE_DIR = Path(__file__).resolve().parent
SOLUTION = BASE_DIR / "2026 gtpc" / "학습준비물" / "solution(linear).py"
TEST_DIR = BASE_DIR / "2026 gtpc" / "학습준비물" / "tests" / "supplies"
TIMEOUT = 10  # 초: 무한 실행 방지
POLL_INTERVAL = 0.005  # 메모리 관측 간격(초)
MIB = 1024 * 1024

def run_case(input_path):
    # 임시 파일로 출력을 받아 PIPE 버퍼가 가득 차 멈추는 현상을 피한다.
    with input_path.open('rb') as stdin, tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        started = time.perf_counter()
        process = subprocess.Popen(
            [sys.executable, str(SOLUTION.resolve())],
            stdin=stdin, stdout=stdout, stderr=stderr,
            cwd=SOLUTION.resolve().parent,
        )
        peak = None
        timed_out = False
        try:
            try:
                monitored = psutil.Process(process.pid)
            except psutil.NoSuchProcess:
                monitored = None
            while True:
                if monitored is not None:
                    try:
                        used = monitored.memory_info().rss
                        peak = used if peak is None else max(peak, used)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                if process.poll() is not None:
                    break
                if time.perf_counter() - started >= TIMEOUT:
                    timed_out = True
                    process.kill()
                    break
                time.sleep(POLL_INTERVAL)
            process.wait()
            elapsed = time.perf_counter() - started
        finally:
            if process.poll() is None:
                process.kill()
            process.wait()
        stdout.seek(0)
        actual = stdout.read().decode('utf-8', errors='replace').split()
        return actual, process.returncode, timed_out, elapsed, peak


def main():
    if not SOLUTION.is_file():
        print(f'풀이 파일이 없습니다: {SOLUTION}')
        return
    inputs = sorted(TEST_DIR.glob('*.in'))
    if not inputs:
        print(f'.in 파일이 없습니다: {TEST_DIR}')
        return
    passed = 0
    for input_path in inputs:
        answer_path = input_path.with_suffix('.ans')
        if not answer_path.is_file():
            print(f'{input_path.name}: 정답 파일 없음')
            continue
        try:
            expected = answer_path.read_text(encoding='utf-8-sig').split()
            actual, code, timed_out, elapsed, peak = run_case(input_path)
            if timed_out:
                status = '시간 초과'
            elif code != 0:
                status = '실행 오류'
            elif actual == expected:
                status = '일치'
                passed += 1
            else:
                status = '불일치'
            memory = '측정 불가' if peak is None else f'{peak / MIB:.2f} MiB'
            print(f'{input_path.name}: {status} | {elapsed:.3f}초 | 최대 관측 메모리 {memory}')
        except OSError as exc:
            print(f'{input_path.name}: 파일/실행 오류: {exc}')
    print(f'\n총 {len(inputs)}개 중 {passed}개 일치')


if __name__ == '__main__':
    main()