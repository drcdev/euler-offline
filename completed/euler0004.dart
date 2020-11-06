import "dart:convert";
import 'dart:math';
import "package:crypto/crypto.dart";

main() {
  String answer = solve();
  String answerMd5 = generateMd5(answer);
  print('Problem 0004');
  print('Answer: $answer');
  print(answerMd5);
  print(checkAnswer(1, answerMd5));
}

String generateMd5(String input) {
  return md5.convert(utf8.encode(input)).toString();
}

bool checkAnswer(int number, String answer) {
  String solution = 'd4cfc27d16ea72a96b83d9bdef6ce2ec';
  return answer == solution;
}

String solve() {
  List<int> values = [];
  for (int x = 1000; x >= 100; x--) {
    for (int y = 1000; y >= 100; y--) {
      int value = x * y;
      if (value.toString() == value.toString().split('').reversed.join()) {
        values.add(value);
      }
    }
  }
  return values.reduce((v, e) => max(v, e)).toString();
}
