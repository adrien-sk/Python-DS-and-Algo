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
return new int[]{};


// List -----------------------------------------------

var list = new List<int>();
list.Add(100);          // O(1)
list.Add(200);          // O(1)
list.Remove(100);       // O(n)
list.Contains(100);     // O(n)
var num = list[1];      // O(1)
var count = list.Count;


// StringBuilder -----------------------------------------------

string str = "The quick brown fox jumps over the lazy dog.";
StringBuilder sb = new StringBuilder(str);
sb.Remove(10, 6); // Remove "brown "
sb.Append("test");
return sb.ToString();