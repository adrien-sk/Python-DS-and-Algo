// Stack -----------------------------------------------

var stack = new Stack<int>();
stack.Push(10);
stack.Pop();
stack.Peek();
var count = stack.Count;


// Queue -----------------------------------------------

var queue = new Queue<int>();
queue.Enqueue(10);
queue.Dequeue();
queue.Peek();
var count = queue.Count;


// HashSet -----------------------------------------------

var hs = new HashSet<int>();
hs.Add(5);
if (hs.Contains(5)) { }
hs.Remove(5);
var count = hs.Count;


// HashMap -----------------------------------------------

var hashMap = new Dictionary<string, int>();
hashMap["apple"] = 10;
hashMap["banana"] = 20;
hashMap["orange"] = 30;
var count = hashMap.Count;

foreach (var pair in hashMap)
{
    Console.WriteLine($"{pair.Key}: {pair.Value}");
}


// Array -----------------------------------------------

var numbers = new int[5] { 10, 20, 30, 40, 50 };
var count = numbers.Length;
var res = new int[3];
//  return new int[] { };

var directions = new (int, int)[]{(0, 1), (0, -1), (1, 0), (-1, 0)};

int[] arr = { 1, 2, 3, 4, 5 };
int[] sub = arr[1..4];

int[,] dp = new int[3, 4]; // 3 rows, 4 columns
dp[2, 3] = 42;
Console.WriteLine(dp.Length);       // 12
Console.WriteLine(dp.GetLength(0)); // 3
Console.WriteLine(dp.GetLength(1)); // 4

int[][] dp = new int[3][];
dp[0] = new int[4];
dp[1][2] = 5;

// List -----------------------------------------------

var list = new List<int>();
list.Add(100);          // O(1)
list.Add(200);          // O(1)
list.Remove(100);       // O(n)
list.Contains(100);     // O(n)
var num = list[1];      // O(1)
var count = list.Count;

List<int> list1 = new List<int> { 1, 2 };
List<int> list2 = new List<int> { 7, 8, 9 };
List<int> new1 = new List<int>(list1) { 7, 8, 9 };

list1.AddRange(list2);



// StringBuilder -----------------------------------------------

string str = "The quick brown fox jumps over the lazy dog.";
StringBuilder sb = new StringBuilder(str);
sb.Remove(10, 6); // Remove "brown "
sb.Append("test");
return sb.ToString();