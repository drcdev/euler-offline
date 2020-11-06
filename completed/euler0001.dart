import "dart:convert";
import "package:crypto/crypto.dart";

main() {
  String answer = solve();
  String answerMd5 = generateMd5(answer);
  print('Problem 0001');
  print('Answer: $answer');
  print(answerMd5);
  print(checkAnswer(1, answerMd5));
}

String generateMd5(String input) {
  return md5.convert(utf8.encode(input)).toString();
}

bool checkAnswer(int number, String answer) {
  String solution = 'e1edf9d1967ca96767dcc2b2d6df69f4';
  return answer == solution;
}

String solve() {
  int sum = 0;
  for (int i = 1; i < 1000; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }
  return sum.toString();
}
