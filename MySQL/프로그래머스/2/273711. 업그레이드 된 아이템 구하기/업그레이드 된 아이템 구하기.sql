-- 코드를 작성해주세요

SELECT 
    C.ITEM_ID, 
    C.ITEM_NAME, 
    C.RARITY
FROM 
    ITEM_INFO P
JOIN 
    ITEM_TREE T ON P.ITEM_ID = T.PARENT_ITEM_ID
JOIN 
    ITEM_INFO C ON T.ITEM_ID = C.ITEM_ID
WHERE 
    P.RARITY = 'RARE'
ORDER BY 
    C.ITEM_ID DESC;

# 부모, 자식 P,C 로 나눠 쿼리 , 서브쿼리로도 풀 수 있음 