import "dart:convert";
import "package:crypto/crypto.dart";

main() {
  String answer = solve();
  String answerMd5 = generateMd5(answer);
  print('Problem 0002');
  print('Answer: $answer');
  print(answerMd5);
  print(checkAnswer(1, answerMd5));
}

String generateMd5(String input) {
  return md5.convert(utf8.encode(input)).toString();
}

bool checkAnswer(int number, String answer) {
  String solution = '4194eb91842c8e7e6df099ca73c38f28';
  return answer == solution;
}

String solve() {
  int sum = 0, x = 1, y = 1;
  while (y < 4000000) {
    if (y % 2 == 0) {
      sum += y;
    }
    int z = y;
    y += x;
    x = z;
  }
  return sum.toString();
}
