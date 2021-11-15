class Solution {
	public List<Boolean> prefixesDivBy5(int[] A) {
		List<Boolean> result = new ArrayList<>(A.length);
		int s = 0;
		for (int i : A)
			result.add((s = (s * 2 + i) % 5) == 0);

		return result;
	}
}
