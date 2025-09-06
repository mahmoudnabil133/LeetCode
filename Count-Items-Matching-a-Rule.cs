public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        var map = new Dictionary<string, int>();
        map["type"] = 0; map["color"] = 1; map["name"] = 2;

        return items.Count(item => item[map[ruleKey]] == ruleValue);
    }
}