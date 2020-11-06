import "dart:convert";
import 'dart:math' as math;
import "package:crypto/crypto.dart";

main() {
  String answer = solve();
  String answerMd5 = generateMd5(answer);
  print('Problem 0003');
  print('Answer: $answer');
  print(answerMd5);
  print(checkAnswer(1, answerMd5));
}

String generateMd5(String input) {
  return md5.convert(utf8.encode(input)).toString();
}

bool checkAnswer(int number, String answer) {
  String solution = '94c4dd41f9dddce696557d3717d98d82';
  return answer == solution;
}

String solve() {
  int n = 600851475143;
  double nRoot = math.sqrt(n);
  List<int> factors = [];
  for (int i = 2; i <= nRoot; i += 1) {
    if (n % i == 0) {
      factors.add(i);
    }
  }
  int i = 0;
  int j = factors.length - 1;
  while (j > i) {
    if (factors[j] % factors[i] == 0) {
      i = 0;
      j = j - 1;
    } else {
      i += 1;
    }
  }
  return factors[j].toString();
}
